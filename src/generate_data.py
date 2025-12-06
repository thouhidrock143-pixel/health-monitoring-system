import pandas as pd
import random
import time
from datetime import datetime

def generate_vital():
    return {
        "timestamp": datetime.now(),
        "heart_rate": random.randint(60, 120),
        "temperature": round(random.uniform(36.0, 39.5), 2),
        "spo2": random.randint(85, 100)
    }

data = []

for _ in range(500):
    data.append(generate_vital())
    time.sleep(0.01)

df = pd.DataFrame(data)
df.to_csv("data/raw_data.csv", index=False)

print("✔ Raw health data generated!")
