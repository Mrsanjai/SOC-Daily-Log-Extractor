from collections import defaultdict

def detect_threat_patterns(parsed_logs):
    alerts = []
    failed_login_count = defaultdict(int)

    for log in parsed_logs:
        if log["type"] == "login_attempt" and log.get("status") == "fail":
            ip = log.get("ip")
            failed_login_count[ip] += 1

            # Alert: Brute-force detection
            if failed_login_count[ip] >= 3:
                alerts.append({
                    "timestamp": log["timestamp"].isoformat(),
                    "alert_type": "Brute Force Attack",
                    "ip": ip,
                    "description": f"3 or more failed login attempts detected from IP {ip}",
                    "severity": "high"
                })
                failed_login_count[ip] = 0  # Reset after alert to avoid flooding

        elif log["type"] == "privilege_escalation":
            alerts.append({
                "timestamp": log["timestamp"].isoformat(),
                "alert_type": "Privilege Escalation Attempt",
                "user": log.get("user"),
                "command": log.get("command"),
                "description": f"Suspicious privilege command: {log.get('command')}",
                "severity": "medium"
            })

        elif log["type"] == "suspicious_process":
            alerts.append({
                "timestamp": log["timestamp"].isoformat(),
                "alert_type": "Suspicious Process Detected",
                "command": log.get("command"),
                "description": f"Suspicious command executed: {log.get('command')}",
                "severity": "medium"
            })

    return alerts
