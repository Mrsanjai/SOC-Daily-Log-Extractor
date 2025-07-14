# app.py
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

ALERTS_FILE = "data/geo_alerts.json"

def load_alerts():
    if not os.path.exists(ALERTS_FILE):
        return []
    with open(ALERTS_FILE, 'r') as f:
        alerts_dict = json.load(f)
        # Sort by timestamp descending
        return sorted(alerts_dict.values(), key=lambda x: x["timestamp"], reverse=True)

@app.route("/")
def home():
    return render_template("dashboard.html", alerts=load_alerts())

if __name__ == "__main__":
    app.run(debug=True, port=5007)
