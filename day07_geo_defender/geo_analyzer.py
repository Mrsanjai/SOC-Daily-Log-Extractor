# geo_analyzer.py
import os
import time
import json
from utils.geoip_lookup import get_geo_data  # ✅ Updated import

LOG_FILE = "logs/login_events.log"
HISTORY_FILE = "data/ip_country_history.json"
ALERTS_FILE = "data/geo_alerts.json"

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        try:
            return json.load(f)
        except:
            return {}

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def monitor_log_file():
    print("[GeoAnalyzer] Watching log file for geo login alerts...")
    seen_lines = set()

    while True:
        time.sleep(2)
        if not os.path.exists(LOG_FILE):
            continue

        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()

        history = load_json(HISTORY_FILE)
        alerts = load_json(ALERTS_FILE)

        for line in lines:
            if line in seen_lines:
                continue

            seen_lines.add(line)
            if "ip=" in line:
                try:
                    ip = line.split("ip=")[1].split(",")[0].strip()
                    user = line.split("user=")[1].split(",")[0].strip()
                    timestamp = line.split("]")[0].replace("[", "")

                    geo_data = get_geo_data(ip)
                    country = geo_data["country"]
                    lat = geo_data["lat"]
                    lon = geo_data["lon"]

                    if user not in history:
                        history[user] = []

                    if country not in history[user]:
                        # New country detected
                        print(f"[ALERT] New country login for {user}: {country} ({ip})")
                        history[user].append(country)

                        alert = {
                            "timestamp": timestamp,
                            "user": user,
                            "ip": ip,
                            "country": country,
                            "lat": lat,
                            "lon": lon
                        }

                        alerts[timestamp] = alert
                        save_json(ALERTS_FILE, alerts)

                    save_json(HISTORY_FILE, history)

                except Exception as e:
                    print(f"[Parse Error] {e}")

if __name__ == "__main__":
    monitor_log_file()
