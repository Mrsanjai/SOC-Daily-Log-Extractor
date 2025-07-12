import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import os

def generate_charts(alerts, output_folder="output/charts"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # ----- Pie Chart: Alert Types -----
    alert_types = [alert['alert_type'] for alert in alerts]
    alert_type_counts = Counter(alert_types)

    plt.figure(figsize=(6, 6))
    plt.pie(alert_type_counts.values(), labels=alert_type_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Alert Type Distribution")
    pie_path = os.path.join(output_folder, "alert_pie.png")
    plt.savefig(pie_path)
    plt.close()

    # ----- Timeline Chart: Alerts over Time -----
    alert_times = [datetime.fromisoformat(alert['timestamp']) for alert in alerts]
    alert_times.sort()
    time_counts = Counter(alert_times)

    plt.figure(figsize=(10, 4))
    plt.plot(list(time_counts.keys()), list(time_counts.values()), marker='o', linestyle='-', color='red')
    plt.title("Alerts Timeline")
    plt.xlabel("Time")
    plt.ylabel("Alert Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    timeline_path = os.path.join(output_folder, "alert_timeline.png")
    plt.savefig(timeline_path)
    plt.close()

    print(f"✅ Charts saved to: {pie_path}, {timeline_path}")
