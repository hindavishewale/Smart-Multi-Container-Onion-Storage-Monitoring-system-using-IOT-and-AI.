import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

rows = []

for _ in range(2200):
    temp     = round(random.uniform(20, 40), 2)
    humidity = round(random.uniform(50, 90), 2)
    moisture = round(humidity * 0.2 + random.uniform(-3, 3), 2)
    co2      = round(temp*10 + moisture*5 + random.uniform(-80, 80), 2)

    high_count = sum([temp > 32, humidity > 75, co2 > 550, moisture > 16])

    near_boundary = (29 < temp < 33 or 63 < humidity < 77 or 380 < co2 < 570)

    if high_count >= 3:
        status = "Critical"
    elif high_count == 2:
        status = "Critical" if not near_boundary else random.choice(["Critical", "Warning"])
    elif high_count == 1:
        status = "Warning"  if not near_boundary else random.choice(["Warning", "Safe", "Critical"])
    else:
        status = "Safe"     if not near_boundary else random.choice(["Safe", "Warning"])

    rows.append([temp, humidity, moisture, co2, status])

df = pd.DataFrame(rows, columns=["Temperature", "Humidity", "Moisture", "CO2", "Status"])

print(f"✅ Dataset generated: {len(df)} rows")
print(df["Status"].value_counts())
df.to_csv("onion_storage_dataset.csv", index=False)
print("💾 Saved to onion_storage_dataset.csv")
