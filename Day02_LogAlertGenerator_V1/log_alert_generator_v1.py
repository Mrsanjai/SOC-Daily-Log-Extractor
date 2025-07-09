# log_alert_generator_v1.py

alert_keywords = ["Failed password", "unauthorized", "Invalid user", "root login"]

with open("system.log", "r") as logfile, open("alerts_output.txt", "w") as alertfile:
    for line in logfile:
        for keyword in alert_keywords:
            if keyword.lower() in line.lower():
                alert_msg = f"[ALERT] Suspicious activity detected: {line.strip()}"
                print(alert_msg)
                alertfile.write(alert_msg + "\n")
                break
