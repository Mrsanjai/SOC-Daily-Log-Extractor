import re
from datetime import datetime

def parse_logs(log_file_path):
    parsed_logs = []

    with open(log_file_path, 'r') as file:
        for line in file:
            log = {}
            # Extract timestamp
            time_match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
            if time_match:
                log["timestamp"] = datetime.strptime(time_match.group(1), "%Y-%m-%d %H:%M:%S")

            # Detect log type
            if "User login attempt" in line:
                log["type"] = "login_attempt"
                user = re.search(r"user=(\w+)", line)
                ip = re.search(r"ip=([\d\.]+)", line)
                status = re.search(r"status=(\w+)", line)
                if user: log["user"] = user.group(1)
                if ip: log["ip"] = ip.group(1)
                if status: log["status"] = status.group(1)

            elif "Privilege escalation attempt" in line:
                log["type"] = "privilege_escalation"
                user = re.search(r"user=(\w+)", line)
                cmd = re.search(r"cmd=(.+)", line)
                if user: log["user"] = user.group(1)
                if cmd: log["command"] = cmd.group(1)

            elif "Suspicious process" in line:
                log["type"] = "suspicious_process"
                cmd = re.search(r"cmd=(.+)", line)
                if cmd: log["command"] = cmd.group(1)

            if log:
                parsed_logs.append(log)

    return parsed_logs
