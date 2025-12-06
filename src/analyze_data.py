import pandas as pd

df = pd.read_csv("data/raw_data.csv", parse_dates=['timestamp'])

df = df[(df['heart_rate'] > 30) & (df['heart_rate'] < 200)]
df = df[(df['temperature'] > 30) & (df['temperature'] < 45)]
df = df[(df['spo2'] > 50) & (df['spo2'] <= 100)]

df['hr_avg'] = df['heart_rate'].rolling(10).mean()
df['temp_avg'] = df['temperature'].rolling(10).mean()
df['spo2_avg'] = df['spo2'].rolling(10).mean()

def alert(row):
    if row['heart_rate'] > 110:
        return "High Heart Rate"
    if row['spo2'] < 92:
        return "Low SpO₂"
    if row['temperature'] > 38:
        return "Fever"
    return "Normal"

df['alert'] = df.apply(alert, axis=1)

df.to_csv("data/cleaned_data.csv", index=False)

print("✔ Data cleaned & analyzed!")
