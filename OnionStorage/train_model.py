import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

df_base = pd.read_csv("onion_storage_dataset.csv")
print(f"📦 Base dataset: {len(df_base)} rows")

TEST_CSV = "sensor_test_data.csv"
if os.path.exists(TEST_CSV):
    df_test = pd.read_csv(TEST_CSV)
    if len(df_test) > 0:
        df_test = df_test[["Temperature", "Humidity", "Moisture", "CO2", "Status"]]
        df_base = pd.concat([df_base, df_test], ignore_index=True)
        print(f"📡 Real sensor data added: {len(df_test)} rows")

print(f"📊 Total training data: {len(df_base)} rows")

X = df_base[["Temperature", "Humidity", "Moisture", "CO2"]]
y = df_base["Status"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\n🔀 Train samples: {len(X_train)}")
print(f"🔀 Test  samples: {len(X_test)}")

model = DecisionTreeClassifier(max_depth=6, min_samples_split=10, min_samples_leaf=5, random_state=42)
model.fit(X_train, y_train)

y_pred         = model.predict(X_test)
train_accuracy = accuracy_score(y_train, model.predict(X_train))
test_accuracy  = accuracy_score(y_test, y_pred)

print(f"\n✅ Training Accuracy : {train_accuracy*100:.2f}%")
print(f"✅ Testing  Accuracy : {test_accuracy*100:.2f}%")
print(f"\n📋 Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Critical", "Safe", "Warning"]))

joblib.dump(model, "model.pkl")
print("💾 model.pkl saved!")
