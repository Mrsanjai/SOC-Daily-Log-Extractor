import json
from core.log_parser import parse_logs
from core.pattern_detector import detect_threat_patterns
from core.alert_visualizer import generate_charts
import os

def main():
    log_file = "data/sample_logs.log"
    output_alerts_file = "output/alerts.json"

    print("🔍 Parsing logs...")
    parsed_logs = parse_logs(log_file)

    print("⚠️ Detecting threat patterns...")
    alerts = detect_threat_patterns(parsed_logs)

    print(f"💾 Saving {len(alerts)} alerts to {output_alerts_file}...")
    os.makedirs(os.path.dirname(output_alerts_file), exist_ok=True)
    with open(output_alerts_file, "w") as f:
        json.dump(alerts, f, indent=4)

    print("📊 Generating visual charts...")
    generate_charts(alerts)

    print("✅ DONE: Threat Pattern Analyzer completed successfully.")

if __name__ == "__main__":
    main()
