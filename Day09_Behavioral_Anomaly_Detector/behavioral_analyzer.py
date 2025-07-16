import pandas as pd
from datetime import datetime
import os

def get_hour(timestamp_str):
    try:
        return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S").hour
    except ValueError:
        return None

def detect_anomalies(input_file, output_dir):
    df = pd.read_csv(input_file)
    df['hour'] = df['timestamp'].apply(get_hour)

    anomalies = []

    for user in df['username'].unique():
        user_data = df[df['username'] == user]
        hours = user_data['hour'].dropna()
        if len(hours) < 3:
            continue  # Not enough data to determine normal range

        lower_bound = hours.quantile(0.25)
        upper_bound = hours.quantile(0.75)

        for idx, row in user_data.iterrows():
            hour = row['hour']
            if hour < lower_bound or hour > upper_bound:
                anomalies.append({
                    "username": row['username'],
                    "timestamp": row['timestamp'],
                    "normal_range": f"{int(lower_bound)}:00–{int(upper_bound)}:00",
                    "anomaly": "✅ Yes"
                })
            else:
                anomalies.append({
                    "username": row['username'],
                    "timestamp": row['timestamp'],
                    "normal_range": f"{int(lower_bound)}:00–{int(upper_bound)}:00",
                    "anomaly": "❌ No"
                })

    anomalies_df = pd.DataFrame(anomalies)
    os.makedirs(output_dir, exist_ok=True)
    anomalies_df.to_csv(os.path.join(output_dir, "anomalies.csv"), index=False)
    print("[+] Anomaly report saved to output/anomalies.csv")

