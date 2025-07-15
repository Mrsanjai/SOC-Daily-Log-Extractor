from flask import Flask, render_template, jsonify
import json
from collections import Counter
import os

app = Flask(__name__)

LOG_PATH = os.path.join("data", "alerts.json")

def extract_ips(log_file):
    with open(log_file, 'r') as f:
        logs = json.load(f)

    ip_list = []
    for log in logs:
        ip = log.get("ip") or log.get("src_ip") or log.get("source")  # adjust key as per log format
        if ip:
            ip_list.append(ip)

    return Counter(ip_list)

@app.route('/')
def index():
    ip_counter = extract_ips(LOG_PATH)
    top_ips = ip_counter.most_common(10)

    labels = [ip for ip, _ in top_ips]
    counts = [count for _, count in top_ips]

    # Risk tagging
    risks = ['High' if c > 10 else 'Medium' if c > 5 else 'Low' for c in counts]

    return render_template('dashboard.html', labels=labels, counts=counts, risks=risks, data=top_ips)

if __name__ == '__main__':
    app.run(debug=True)
