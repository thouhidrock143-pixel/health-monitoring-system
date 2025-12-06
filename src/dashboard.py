import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏥 Health Monitoring Analytics Dashboard")

df = pd.read_csv("data/cleaned_data.csv")

st.subheader("📈 Heart Rate (BPM)")
fig1 = px.line(df, x="timestamp", y="heart_rate")
st.plotly_chart(fig1)

st.subheader("🌡 Body Temperature (°C)")
fig2 = px.line(df, x="timestamp", y="temperature")
st.plotly_chart(fig2)

st.subheader("🩸 SpO₂ (%)")
fig3 = px.line(df, x="timestamp", y="spo2")
st.plotly_chart(fig3)

st.subheader("⚠ Alerts")
alert_df = df[df['alert'] != "Normal"]
st.dataframe(alert_df)
