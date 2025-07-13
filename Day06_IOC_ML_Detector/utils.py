# utils.py

import json
from datetime import datetime
import time

ALERTS_FILE = "alerts.json"

def init_alerts_file():
    try:
        with open(ALERTS_FILE, "r", encoding="utf-8") as f:
            json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(ALERTS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)

def save_alert(alert):
    try:
        with open(ALERTS_FILE, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.append(alert)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
    except (FileNotFoundError, json.JSONDecodeError):
        with open(ALERTS_FILE, "w", encoding="utf-8") as f:
            json.dump([alert], f, indent=2)
