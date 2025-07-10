import requests
import os

INPUT_FILE = '../input/login.log'
ALERT_OUTPUT_FILE = '../output/geo_alerts.txt'
HTML_OUTPUT_FILE = '../output/geo_alerts_report.html'
TEMPLATE_FILE = '../templates/geo_alert_template.html'

INDIAN_COUNTRY_NAME = "India"


def get_country(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        return data.get("country", "Unknown")
    except Exception as e:
        print(f"[!] Error fetching country for IP {ip_address}: {e}")
        return "Unknown"


def parse_log_line(line):
    try:
        parts = line.strip().split(" - ")
        timestamp, user, ip = parts
        return timestamp, user, ip
    except ValueError:
        return None, None, None


def detect_suspicious_logins():
    suspicious_entries = []

    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()

    for line in lines:
        timestamp, user, ip = parse_log_line(line)
        if not ip:
            continue
        country = get_country(ip)

        if country != INDIAN_COUNTRY_NAME:
            entry = {
                "timestamp": timestamp,
                "user": user,
                "ip": ip,
                "country": country
            }
            suspicious_entries.append(entry)

    return suspicious_entries


def write_alerts_to_txt(alerts):
    with open(ALERT_OUTPUT_FILE, 'w') as f:
        for alert in alerts:
            f.write(f"Suspicious Login - Time: {alert['timestamp']} | User: {alert['user']} | IP: {alert['ip']} | Country: {alert['country']}\n")
    print(f"[+] geo_alerts.txt written with {len(alerts)} suspicious entries.")


def generate_html_report(alerts):
    if not os.path.exists(TEMPLATE_FILE):
        print("[!] HTML template not found. Skipping HTML report.")
        return

    from jinja2 import Template

    with open(TEMPLATE_FILE, 'r') as file:
        template = Template(file.read())

    html_content = template.render(alerts=alerts)

    with open(HTML_OUTPUT_FILE, 'w') as f:
        f.write(html_content)

    print(f"[+] geo_alerts_report.html generated.")


if __name__ == "__main__":
    print("[*] Starting GeoAlertor...")
    alerts = detect_suspicious_logins()
    if alerts:
        write_alerts_to_txt(alerts)
        generate_html_report(alerts)
    else:
        print("[✓] No suspicious foreign logins found.")
