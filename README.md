# Smart-Multi-Container-Onion-Storage-Monitoring-system-using-IOT-and-AI.
# 🧅 Smart Multi-Container Onion Storage Monitoring System using IoT and AI

An advanced AI-powered IoT-based onion storage monitoring system designed to reduce onion spoilage, monitor environmental conditions in real time, and improve storage management efficiency using machine learning and smart automation.

---

# 📌 Project Overview

The Smart Multi-Container Onion Storage Monitoring System is an intelligent storage management solution that combines:

- Internet of Things (IoT)
- Artificial Intelligence (AI)
- Machine Learning
- Real-Time Sensor Monitoring
- Flask Web Dashboard
- ESP8266 Communication
- Automated Environmental Analysis

The system continuously monitors onion storage conditions using multiple sensors connected to ESP8266 NodeMCU devices.

Sensor data is transmitted to a Flask-based backend server where:
- Environmental conditions are analyzed
- Spoilage risk is predicted
- Historical records are stored
- Real-time dashboards are updated
- Alerts are generated automatically

The system helps:
- Farmers
- Storage operators
- Agricultural industries
- Warehouse managers

reduce onion spoilage and maintain optimal storage conditions.

---

# 🎯 Main Objectives

- Reduce onion spoilage during storage
- Monitor multiple storage containers simultaneously
- Detect unsafe environmental conditions
- Predict spoilage risk using AI
- Provide real-time analytics and visualization
- Automate environmental monitoring
- Maintain proper temperature and humidity

---

# 🧠 Problem Statement

Traditional onion storage systems lack:
- Real-time monitoring
- Automated spoilage detection
- AI-based prediction systems
- Environmental analytics
- Multi-container management

As a result:
- Large quantities of onions spoil
- Storage conditions remain unmanaged
- Farmers face financial losses

This project solves these issues using IoT and AI technologies.

---

# ⚙️ System Architecture

## System Workflow

```text
Sensors → ESP8266 → Flask Server → AI Model → Dashboard → Alerts
```

---

# 🔌 Hardware Components

| Component | Purpose |
|---|---|
| ESP8266 NodeMCU | WiFi-enabled microcontroller |
| DHT11 Sensor | Temperature and humidity monitoring |
| MQ135 Sensor | Gas level detection |
| Moisture Sensor | Moisture level detection |
| Relay Module | Controls cooling system/fan |
| Cooling Fan | Temperature control |
| Breadboard & Wires | Circuit connections |

---

# 💻 Software Technologies

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web framework |
| HTML | Frontend structure |
| CSS | Styling |
| JavaScript | Dynamic updates |
| Bootstrap | Responsive UI |
| Pandas | Data processing |
| NumPy | Numerical computation |
| Scikit-learn | Machine learning |
| CSV Storage | Sensor data logging |

---

# 🌐 Features

# ✅ Real-Time Monitoring

The dashboard continuously monitors:

- Temperature
- Humidity
- Gas concentration
- Moisture levels
- CO₂ concentration

Sensor readings update automatically in real time.

---

# ✅ Multi-Container Monitoring

The system supports multiple onion storage blocks.

Example:

| Block | Status |
|---|---|
| Block 1 | No Data |
| Block 2 | Safe |

Each block has:
- Independent monitoring
- Separate analytics
- Individual status tracking

---

# ✅ AI-Based Spoilage Detection

The AI model analyzes environmental conditions and predicts:

- Safe
- Warning
- Critical

The prediction system helps detect spoilage risks before damage occurs.

---

# ✅ Interactive Dashboard

The OnionStore dashboard provides:

- Live sensor readings
- Status overview
- Analytics charts
- Block comparison
- Historical data
- Alert management

---

# ✅ Analytics Page

Displays:
- Temperature graphs
- Humidity analysis
- Status distribution
- Block-wise comparison
- Environmental trends

---

# ✅ Alerts System

The system generates alerts when:
- Temperature becomes unsafe
- Humidity exceeds threshold
- Gas levels rise
- CO₂ concentration increases

Alert categories:
- Safe
- Warning
- Critical

---

# ✅ Historical Data Tracking

All sensor readings are stored in CSV format.

Features:
- Historical monitoring
- Data analysis
- Trend detection
- Model retraining dataset

---

# ✅ AI Model Retraining

Collected sensor data is used to improve prediction accuracy.

Retrain model using:

```bash
python train_model.py
```

---

# 📊 Dashboard Overview

The dashboard includes:

## 🧅 Storage Dashboard
Displays:
- Total blocks
- Safe blocks
- Average temperature
- Average humidity

---

## 📦 Storage Blocks

Each block displays:
- Status
- Temperature
- Humidity
- Moisture
- CO₂ levels
- Fan status

Example:

```text
🧅 Block 2
Status: Safe
Temperature: 27.0°C
Humidity: 62.0%
Moisture: 12.4
CO₂ ppm: 380.0
Fan: OFF
```

---

## 📈 Analytics Section

Displays:
- Temperature & humidity charts
- Status distribution
- Block status overview

---

# 📁 Project Structure

```text
Smart-Multi-Container-Onion-Storage-Monitoring-system-using-IOT-and-AI/
│
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
├── README.md
├── sensor_test_data.csv
├── sensor_history.csv
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
├── templates/
│   ├── dashboard.html
│   ├── analytics.html
│   ├── alerts.html
│   ├── history.html
│   ├── testdata.html
│   ├── settings.html
│   └── about.html
│
├── esp8266/
│   └── esp_code.ino
│
└── dataset/
    └── training_data.csv
```

---

# 🔥 Machine Learning Model

The ML model predicts onion storage conditions based on:

- Temperature
- Humidity
- Gas concentration
- Moisture
- CO₂ levels

---

# 📌 Prediction Categories

| Category | Meaning |
|---|---|
| Safe | Storage conditions are normal |
| Warning | Conditions may become unsafe |
| Critical | High spoilage risk |

---

# 📡 API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Main dashboard |
| `/analytics` | Analytics page |
| `/alerts` | Alerts page |
| `/history` | Sensor history |
| `/testdata` | Test data page |
| `/api/testdata` | JSON sensor data |
| `/api/history` | Historical sensor data |

---

# 🚀 Installation Guide

# Step 1 — Clone Repository

```bash
git clone https://github.com/hindavishewale/Smart-Multi-Container-Onion-Storage-Monitoring-system-using-IOT-and-AI.git
```

---

# Step 2 — Move into Project Folder

```bash
cd Smart-Multi-Container-Onion-Storage-Monitoring-system-using-IOT-and-AI
```

---

# Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 4 — Run Flask Server

```bash
python app.py
```

---

# Step 5 — Open Browser

```text
http://127.0.0.1:5000
```

---

# 📦 requirements.txt

```text
flask
pandas
numpy
scikit-learn
joblib
matplotlib
gunicorn
```

---

# 🔐 Future Enhancements

- Cloud database integration
- Mobile application
- SMS alert system
- Email notifications
- Camera-based onion quality analysis
- Deep learning prediction model
- Automatic fan control
- Remote monitoring application

---

# 📷 Screenshots

## Dashboard

Add dashboard screenshot here.

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

# 🌍 Deployment Platforms

The project can be deployed on:

- Render
- Railway
- PythonAnywhere
- AWS
- Heroku

---

# 👩‍💻 Author

# Hindavi Shewale

Computer Engineering Student  
Passionate about:
- AI/ML
- IoT
- Web Development
- Intelligent Monitoring Systems

---



# 📜 License

This project is developed for:
- Educational purposes
- Research purposes
- Academic innovation

---

# 🙌 Acknowledgement

Special thanks to:
- Open-source community
- Flask documentation
- ESP8266 IoT ecosystem
- Machine learning libraries

---

# 🧅 OnionStore Monitoring System

AI + IoT + Real-Time Spoilage Detection
