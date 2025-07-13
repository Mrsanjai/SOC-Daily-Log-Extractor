# main.py

import time, json, threading
from ioc_detector import detect_ioc
from anomaly_detector import AnomalyDetector
from utils import save_alert, init_alerts_file
from datetime import datetime

LOG_FILE = "logs/sysmon_live.log"

detector = AnomalyDetector()
detector.train(LOG_FILE)
init_alerts_file()

def process_line(line):
    print("[DEBUG]", line)  # ⬅️ Add this to confirm lines are read
    alerts = []

    ioc_alert = detect_ioc(line)
    if ioc_alert:
        print("[IOC ALERT]", ioc_alert["summary"])
        alerts.append(ioc_alert)

    if detector.trained and detector.is_anomalous(line):
        summary = f"🤖 ML anomaly: {line[:80]}"
        ml_alert = {
            "id": f"ml-{int(time.time())}",
            "ioc": "anomaly",
            "source": "AnomalyDetector",
            "timestamp": datetime.utcnow().isoformat(),
            "summary": summary,
            "status": "new",
            "severity": "high",
            "mitre_tactic": "Unknown",
            "mitre_technique": "N/A"
        }
        print("[ML ALERT]", summary)
        alerts.append(ml_alert)

    for alert in alerts:
        save_alert(alert)

def tail_log():
    with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                process_line(line.strip())
            else:
                time.sleep(1)

if __name__ == "__main__":
    print("[*] Starting IOC + ML Detector...")
    t = threading.Thread(target=tail_log)
    t.start()
