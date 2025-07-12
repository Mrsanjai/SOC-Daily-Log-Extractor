from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    with open("output/alerts.json") as f:
        alerts = json.load(f)
    return render_template("dashboard.html", alerts=alerts)

@app.route("/api/alerts")
def alert_api():
    with open("output/alerts.json") as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(debug=True)
