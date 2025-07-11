from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='threading')

ALERT_FILE = '../output/alerts.json'

def load_alerts():
    if os.path.exists(ALERT_FILE):
        with open(ALERT_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("⚠️ JSON error in alerts file")
                return []
    return []

@app.route('/')
def index():
    alerts = load_alerts()
    stats = {
        "total_alerts": len(alerts),
        "unique_ips": len(set(alert['ip'] for alert in alerts)),
        "types": list(set(alert['type'] for alert in alerts))
    }
    return render_template('index.html', alerts=alerts, stats=stats)


@socketio.on('connect')
def on_connect():
    print("[🔌] Client connected")

if __name__ == '__main__':
    print("[⚡] Starting live alert dashboard...")
    print("🌐 Open http://localhost:5000/")
    socketio.run(app, debug=True, host='127.0.0.1', port=5000)
