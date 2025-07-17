import datetime
import json
import os

def load_suspicious_devices(file_path='suspicious_usb_devices.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data["suspicious_devices"]

def is_outside_business_hours(timestamp):
    dt = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    return dt.hour < 9 or dt.hour > 19

def detect_usb_anomalies(log_file_path, output_path="alerts_output.txt"):
    if not os.path.exists(log_file_path):
        return ["❌ Log file not found."]
    
    suspicious_devices = load_suspicious_devices()
    alerts = []

    with open(log_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        try:
            # Example line:
            # 2025-07-16 03:15:42, USB Inserted, Device Name: Unknown, VID: 0BAD, PID: CAFE, User: admin
            parts = line.strip().split(',')
            timestamp = parts[0].strip()
            action = parts[1].strip()
            user = ""
            device_name, vid, pid = "", "", ""

            for part in parts[2:]:
                if "Device Name" in part:
                    device_name = part.split(":")[1].strip()
                elif "VID" in part:
                    vid = part.split(":")[1].strip().upper()
                elif "PID" in part:
                    pid = part.split(":")[1].strip().upper()
                elif "User" in part:
                    user = part.split(":")[1].strip()

            # Skip if not a USB insert
            if "Inserted" not in action:
                continue

            # Check for suspicious VID/PID
            for dev in suspicious_devices:
                if dev["vendor_id"] == vid and dev["product_id"] == pid:
                    alerts.append(f"⚠️ {timestamp}: Suspicious device detected ({dev['label']}) by {user} - VID:{vid}, PID:{pid}")
                    break

            # Check for off-hour access
            if is_outside_business_hours(timestamp):
                alerts.append(f"⏰ {timestamp}: USB inserted outside business hours by {user} - Device: {device_name}")

        except Exception as e:
            alerts.append(f"❌ Error parsing line: {line.strip()} | Error: {str(e)}")

    if alerts:
        with open(output_path, 'w', encoding='utf-8') as f:
            for alert in alerts:
                f.write(alert + "\n")

    return alerts if alerts else ["✅ No suspicious USB activity detected."]
