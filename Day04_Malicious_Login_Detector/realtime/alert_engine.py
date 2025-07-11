import re
import json
import os
from flask_socketio import SocketIO

ALERT_FILE = '../output/alerts.json'

# Optional: you can make this a shared memory if needed
failed_logins = {}

def emit_alert(alert):
    # Emits to WebSocket (optional if inside Flask context)
    try:
        from socket_server import socketio
        socketio.emit('new_alert', alert)
    except:
        pass

def process_log_line(line):
    ip_match = re.search(r'from ([\d\.]+)', line)
    if not ip_match:
        return
    ip = ip_match.group(1)

    alert = None

    if "Failed password" in line:
        failed_logins[ip] = failed_logins.get(ip, 0) + 1
        if failed_logins[ip] >= 3:
            alert = {
                "type": "Brute Force Attempt",
                "ip": ip,
                "fail_count": failed_logins[ip],
                "line": line.strip()
            }

    elif "Accepted password" in line and failed_logins.get(ip, 0) >= 3:
        alert = {
            "type": "Suspicious Login After Failures",
            "ip": ip,
            "fail_count": failed_logins[ip],
            "line": line.strip()
        }

    if alert:
        print(f"[⚠️] Alert Detected: {alert}")
        save_alert(alert)
        emit_alert(alert)

def save_alert(alert):
    if os.path.exists(ALERT_FILE):
        with open(ALERT_FILE, 'r') as f:
            try:
                existing = json.load(f)
            except:
                existing = []
    else:
        existing = []

    existing.append(alert)
    with open(ALERT_FILE, 'w') as f:
        json.dump(existing, f, indent=4)
