### 📅 Day 3 – GeoAlertor: Foreign Login Detector 🌍

- 🚨 Detects suspicious logins from IPs **outside India**
- 🌐 Uses `ip-api.com` for IP geolocation
- 📄 Outputs alerts in `.txt` and optional `.html` format
- 📁 [`Day03_GeoAlertor`](./Day03_GeoAlertor/)

---

## 🧠 Features
- Parses login logs with user + IP
- Uses `ip-api.com` to find the IP's country
- Flags IPs not from **India**
- Generates:
  - 📄 `geo_alerts.txt` with suspicious entries
  - 🌐 `geo_alerts_report.html` for visual analysis

---

## 📂 Folder Structure
Day03_GeoAlertor/
├── core/
│ └── log_geo_alertor.py
├── input/
│ └── login.log
├── output/
│ ├── geo_alerts.txt
│ └── geo_alerts_report.html
├── templates/
│ └── geo_alert_template.html
├── README.md
├── requirements.txt
└── .gitignore


---

## ⚙️ How to Use

1. 📥 Put your login log in `input/login.log`:


2. ▶️ Run the script:

   bash
cd core
python log_geo_alertor.py

pip install -r requirements.txt

Screenshot:

![log1](https://github.com/user-attachments/assets/74266c4a-e66b-465f-8302-36ca08650cd0)
![log](https://github.com/user-attachments/assets/b7acd937-e723-4eaf-b494-b0469caaf046)

🌐 API Used
ip-api.com – Free IP Geolocation API

🔒 Note
This tool assumes India as the safe zone. You can change INDIAN_COUNTRY_NAME in the code to localize it for any country.

Sanjai R 
– Cybersecurity Career Domination | Day 3 of 6-Month SOC Journey
#sanjai #sanjaicyber #sanjaicybersecurity
#soc #cyber #cybersecurity
