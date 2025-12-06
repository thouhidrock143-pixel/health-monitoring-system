<!-- Banner -->
<p align="center">
  <img src="https://raw.githubusercontent.com/thouhidrock143-pixel/health-monitoring-system/main/health-2.png" width="80%">
</p>

# 🩺 Real-Time Health Monitoring & Data Analytics System  

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow?style=for-the-badge&logo=pandas)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-orange?style=for-the-badge&logo=numpy)](https://numpy.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-purple?style=for-the-badge&logo=plotly)](https://plotly.com/)

A complete health-data analytics system simulating and analyzing real-time vital signs (Heart Rate, Temperature, SpO₂).  
This system detects anomalies, generates alerts, cleans data, and visualizes insights using an interactive Streamlit dashboard.  
Perfect for **Data Analyst portfolio**, **Healthcare Analytics**, or **IoT data simulation projects**.

---

## 🚀 Features  

### 🔹 1. Real-Time Vital Sign Simulation  
Generates realistic health data:  
- Heart Rate (BPM)  
- Body Temperature (°C)  
- Blood Oxygen (SpO₂ %)  

**Saved as:** `data/raw_data.csv`

---

### 🔹 2. Data Cleaning & Preprocessing  
- Removes invalid values  
- Fixes missing entries  
- Creates rolling averages for smooth trends  
- Standardizes all measurement fields  

**Output:** `data/cleaned_data.csv`

---

### 🔹 3. Anomaly Detection  
Automatically flags abnormal patterns:  
- 🔥 Fever → Temp > 38°C  
- 💓 High HR → > 110 BPM  
- 🫁 Low SpO₂ → < 92%  

---

### 🔹 4. Interactive Streamlit Dashboard  
Visualizes:  
- Heart Rate Trend  
- Temperature Trend  
- SpO₂ Levels  
- Live Alerts Table  

Run it using:

streamlit run src/dashboard.py


## 🧠 Skills Demonstrated (For Data Analyst Roles)

| Skill Area | Description |
|-----------|-------------|
| **Data Cleaning** | Removing noise, handling invalid readings, fixing missing data |
| **Time-Series Analysis** | Rolling averages, trend detection, baseline comparison |
| **Exploratory Data Analysis** | Identifying patterns and anomalies |
| **Visualization** | Plotly interactive graphs + Streamlit dashboard |
| **Python Scripting** | Modular code for generation, analysis, dashboard |
| **Healthcare Analytics** | Vital signs interpretation & alert logic |

---

## 📁 Project Structure  
health-monitoring-system/  
 │── data/  
 
 │ ├── raw_data.csv
 
 │ └── cleaned_data.csv
 
 │
│── src/

│ ├── generate_data.py

│ ├── analyze_data.py

│ └── dashboard.py

│
│── README.md

│── requirements.txt

---

## ▶️ How to Run  

### 1️⃣ Install dependencies

### 2️⃣ Generate data

### 3️⃣ Analyze & clean data

---

## 🎯 Ideal For  

- Data Analyst portfolio projects  
- Healthcare / medical data analysis  
- IoT + sensor data simulation  
- Time-series analytics practice  
- Streamlit dashboard development  

---

## 👤 Author  

**Shaik Thouhid Basha**  
_Data Analyst • Python • Visualization • Healthcare Analytics_  
GitHub: https://github.com/thouhidrock143-pixel  

---



