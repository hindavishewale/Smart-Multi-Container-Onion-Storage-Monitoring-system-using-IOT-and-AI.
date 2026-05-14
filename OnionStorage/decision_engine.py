# decision_engine.py
# Rule-based + AI decision engine for IoT actuator control

def get_actions(temp, humidity, co2):
    """
    Returns IoT actuator commands and recommended actions
    based on sensor thresholds.
    """
    actions = []
    actuators = {
        "cooling_fan":   False,
        "dehumidifier":  False,
        "exhaust_fan":   False,
    }

    if temp > 32:
        actuators["cooling_fan"] = True
        actions.append("🌀 Cooling Fan ON — Temperature too high")

    if humidity > 75:
        actuators["dehumidifier"] = True
        actions.append("💧 Dehumidifier ON — Humidity too high")

    if co2 > 550:
        actuators["exhaust_fan"] = True
        actions.append("💨 Exhaust Fan ON — CO₂ level critical")

    # All systems on if multiple triggers
    if all(actuators.values()):
        actions.append("⚠️ All systems activated — Emergency ventilation mode")

    if not actions:
        actions.append("✅ All parameters normal — No action required")

    return {
        "actuators": actuators,
        "actions": actions
    }


def get_risk_level(status):
    """Map status string to color and risk label."""
    mapping = {
        "Safe":     {"color": "#27ae60", "risk_label": "Low Risk"},
        "Warning":  {"color": "#f39c12", "risk_label": "Medium Risk"},
        "Critical": {"color": "#e74c3c", "risk_label": "High Risk"},
    }
    return mapping.get(status, {"color": "#9b59b6", "risk_label": "Unknown"})
