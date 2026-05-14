from flask import Flask, render_template, request, jsonify
import joblib
import random
import pandas as pd
import os
from datetime import datetime
from decision_engine import get_actions, get_risk_level

app = Flask(__name__, static_folder='Statics', static_url_path='/static')

# ── Load model ──
model = joblib.load("model.pkl")

# ── Latest IoT data per block ──
iot_data = {1: None, 2: None}

# ── Test data CSV path ──
TEST_CSV = "sensor_test_data.csv"
if not os.path.exists(TEST_CSV):
    pd.DataFrame(columns=[
        "timestamp", "block_id",
        "Temperature", "Humidity", "Gas",
        "Moisture", "CO2", "Status"
    ]).to_csv(TEST_CSV, index=False)


def derive_features(temp, humidity, gas):
    """Calculate Moisture and CO2 from raw sensor values."""
    moisture = round(humidity * 0.2 + random.uniform(-1, 1), 2)
    co2      = round((gas / 1024) * 800 + temp * 5, 2)
    return moisture, co2


def get_status_label(temp, humidity, co2):
    """Rule-based status — same logic used to train the model."""
    if temp > 32 or humidity > 75 or co2 > 550:
        return "Critical"
    elif temp > 28 or humidity > 65 or co2 > 400:
        return "Warning"
    return "Safe"


def save_to_test_csv(block_id, temp, humidity, gas, moisture, co2, status):
    """Append one sensor reading row, keep max 5000 rows."""
    row = pd.DataFrame([{
        "timestamp":   datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "block_id":    block_id,
        "Temperature": temp,
        "Humidity":    humidity,
        "Gas":         gas,
        "Moisture":    moisture,
        "CO2":         co2,
        "Status":      status
    }])
    row.to_csv(TEST_CSV, mode='a', header=False, index=False)
    df = pd.read_csv(TEST_CSV)
    if len(df) > 5000:
        df.tail(5000).to_csv(TEST_CSV, index=False)


def predict_block(temp, humidity, moisture, co2):
    """Run AI model prediction + confidence %."""
    features = [[temp, humidity, moisture, co2]]
    status   = model.predict(features)[0]
    proba    = model.predict_proba(features)[0]
    risk_pct = round(max(proba) * 100, 1)
    return status, risk_pct


def build_block_data(temp, humidity, gas, moisture, co2):
    """Build full block dict with prediction + engine output."""
    status, risk_pct = predict_block(temp, humidity, moisture, co2)
    risk   = get_risk_level(status)
    engine = get_actions(temp, humidity, co2)
    return {
        "temp":       round(temp, 2),
        "humidity":   round(humidity, 2),
        "gas":        round(gas, 2),
        "moisture":   round(moisture, 2),
        "co2":        round(co2, 2),
        "status":     status,
        "risk_pct":   risk_pct,
        "risk_label": risk["risk_label"],
        "color":      risk["color"],
        "actions":    engine["actions"],
        "actuators":  engine["actuators"]
    }


def generate_data(block_id=None):
    """Block 1 = real ESP. Block 2 = simulated until second ESP connects."""
    if block_id and iot_data.get(block_id):
        d        = iot_data[block_id]
        temp     = d["temp"]
        humidity = d["humidity"]
        gas      = d["gas"]
        moisture, co2 = derive_features(temp, humidity, gas)
        return build_block_data(temp, humidity, gas, moisture, co2)

    # Block 2 simulation when no real ESP connected
    if block_id == 2:
        temp, humidity, gas = 27.0, 62.0, 420.0
        moisture, co2 = 12.4, 380.0
        return build_block_data(temp, humidity, gas, moisture, co2)

    return {
        "temp": None, "humidity": None, "gas": None,
        "moisture": None, "co2": None,
        "status": "No Data", "risk_pct": 0,
        "risk_label": "No Data", "color": "#aaa",
        "actions": ["⏳ Waiting for ESP sensor data..."],
        "actuators": {"cooling_fan": False, "dehumidifier": False, "exhaust_fan": False}
    }


# ══════════════ ROUTES ══════════════

# ── Page routes ──
@app.route('/')
def index():
    blocks = [generate_data(i+1) for i in range(2)]
    return render_template("index.html", blocks=blocks)

@app.route('/analytics')
def analytics(): return render_template("analytics.html")

@app.route('/alerts')
def alerts(): return render_template("alerts.html")

@app.route('/history')
def history(): return render_template("history.html")

@app.route('/testdata')
def testdata(): return render_template("testdata.html")

@app.route('/iot')
def iot(): return render_template("iot.html")

@app.route('/settings')
def settings(): return render_template("settings.html")

@app.route('/about')
def about(): return render_template("about.html")


@app.route('/block/<int:id>')
def detail(id):
    data = generate_data(id)
    return render_template("detail.html", data=data, id=id)


# ── /predict  ← ESP8266 sends here ──
# ESP JSON: {"temperature":30.5, "humidity":72, "co2":850}
# ESP uses block_id via query param or defaults to 1
@app.route('/predict', methods=['POST'])
def predict():
    d = request.get_json(force=True)

    # ESP sends: temperature, humidity, co2
    temp     = float(d.get("temperature", d.get("temp", 0)))
    humidity = float(d.get("humidity", 0))
    gas      = float(d.get("co2", 0))       # ESP calls it co2, it's raw MQ135 value
    block_id = int(d.get("block_id", 1))    # default block 1

    # Derive moisture & storage days
    moisture, co2_ppm = derive_features(temp, humidity, gas)
    status = get_status_label(temp, humidity, co2_ppm)
    save_to_test_csv(block_id, temp, humidity, gas, moisture, co2_ppm, status)
    if block_id in iot_data:
        iot_data[block_id] = {"temp": temp, "humidity": humidity, "gas": gas}
    result = build_block_data(temp, humidity, gas, moisture, co2_ppm)

    # ESP reads plain text response — return status as plain string
    # so ESP strstr(buffer, "Critical") works correctly
    return result["status"] + "\n", 200, {"Content-Type": "text/plain"}


# ── /iot/data  ← alternative endpoint (JSON response) ──
@app.route('/iot/data', methods=['POST'])
def iot_receive():
    d = request.get_json(force=True)
    block_id = int(d.get("block_id", 1))
    if block_id not in [1, 2]:
        return jsonify({"error": "Invalid block_id"}), 400

    temp     = float(d.get("temperature", d.get("temp", 0)))
    humidity = float(d.get("humidity", 0))
    gas      = float(d.get("co2", d.get("gas", 0)))

    moisture, co2_ppm = derive_features(temp, humidity, gas)
    status = get_status_label(temp, humidity, co2_ppm)
    save_to_test_csv(block_id, temp, humidity, gas, moisture, co2_ppm, status)
    iot_data[block_id] = {"temp": temp, "humidity": humidity, "gas": gas}
    result = build_block_data(temp, humidity, gas, moisture, co2_ppm)

    return jsonify({
        "block_id":  block_id,
        "status":    result["status"],
        "risk_pct":  result["risk_pct"],
        "risk":      result["risk_label"],
        "actions":   result["actions"],
        "actuators": result["actuators"]
    })


# ── API for dashboard auto-refresh ──
@app.route('/api/blocks')
def api_blocks():
    blocks = [generate_data(i+1) for i in range(2)]
    return jsonify(blocks)


# ── View saved test data ──
@app.route('/api/testdata')
def view_test_data():
    if os.path.exists(TEST_CSV):
        try:
            df = pd.read_csv(TEST_CSV, header=None, names=[
                "timestamp", "block_id",
                "Temperature", "Humidity", "Gas",
                "Moisture", "CO2", "Status", "extra"
            ])
            df = df.drop(columns=["extra"], errors="ignore")
            df = df[df["Temperature"].notna()]
            df = df[df["Status"].notna()]
            return jsonify(df.tail(50).to_dict(orient='records'))
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify([])


# Port 8000 matches ESP8266 code: const int PORT = 8000
app.run(host='0.0.0.0', port=8000, debug=True)