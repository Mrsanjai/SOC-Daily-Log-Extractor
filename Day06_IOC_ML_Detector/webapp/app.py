# webapp/app.py

from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)
ALERTS_FILE = os.path.join(os.path.dirname(__file__), "..", "alerts.json")

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/alerts")
def get_alerts():
    try:
        with open(ALERTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return jsonify(data[:50])  # Limit to 50 alerts
    except Exception as e:
        return jsonify([])

if __name__ == "__main__":
    app.run(debug=True, port=5001)
