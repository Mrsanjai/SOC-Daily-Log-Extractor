from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

ALERTS_FILE = '../output/alerts.json'

def load_alerts():
    if os.path.exists(ALERTS_FILE):
        try:
            with open(ALERTS_FILE, 'r') as f:
                data = f.read().strip()
                if not data:
                    return []  # Return empty list if file is empty
                return json.loads(data)
        except json.JSONDecodeError:
            print("[!] alerts.json is invalid JSON.")
            return []
    return []


@app.route('/')
def index():
    alerts = load_alerts()
    total_alerts = len(alerts)
    unique_ips = list(set([a['ip'] for a in alerts]))
    alert_types = set([a['type'] for a in alerts])

    stats = {
        'total_alerts': total_alerts,
        'unique_ips': len(unique_ips),
        'types': list(alert_types)
    }

    return render_template('index.html', alerts=alerts, stats=stats)

@app.route('/api/alerts')
def api_alerts():
    return jsonify(load_alerts())

if __name__ == '__main__':
    app.run(debug=True)
