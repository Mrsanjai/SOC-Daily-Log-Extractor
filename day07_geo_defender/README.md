 🌍 Day 07 – GeoDefender

A real-time suspicious login detection and alert dashboard that maps unusual logins across countries using IP geolocation and visualizes them on a live Leaflet-based world map.

---

 🚀 Project Overview

GeoDefender monitors login events in real-time from login_events.log.  
If a user logs in from a new country not seen before, an alert is generated and plotted on an interactive map using latitude/longitude lookup via ip-api.

---

 🎯 Key Features

✅ Real-time monitoring of login logs  
✅ Detects geo-based anomalies (new country per user)  
✅ Interactive world map with country pins  
✅ Flask dashboard with dark-themed Soft UI  
✅ Alerts table with timestamp, user, IP, country  
✅ Lightweight and easy to run anywhere

---

🛠️ Tech Stack

| Component         | Tech                          |
|------------------|-------------------------------|
| 🌐 Web Framework  | Flask                         |
| 🌍 Map Library     | Leaflet.js + OpenStreetMap    |
| 🌎 IP Lookup API   | http://ip-api.com             |
| 🐍 Backend         | Python 3                      |
| 📄 Data Storage    | JSON (alert history, geo info)|
| 🎨 Frontend        | HTML + CSS + Jinja2 Templating|

---

 📂 Folder Structure

day07_geo_defender/

├── app.py                         # Flask dashboard  

├── geo_analyzer.py               # Real-time log parser + geo alert generator  

├── logs/  

│   └── login_events.log          # Simulated login events  

├── data/  

│   ├── geo_alerts.json           # Stores triggered alerts  

│   └── ip_country_history.json   # Tracks login countries per user  

├── templates/  

│   └── dashboard.html            # Beautiful Soft UI + map dashboard  

└── utils
    └── geoip_lookup.py           # Gets country, lat, lon from IP  
    


---

🔁 How It Works

1. geo_analyzer.py watches login_events.log  
2. On every new login line:
   - Extracts user, ip, and timestamp
   - Queries ip-api.com to get country, lat, lon
   - If new country → generate alert + add to geo_alerts.json  
3. app.py runs a Flask app:
   - Reads alert data and shows:
     - 📍 Interactive Leaflet map with markers
     - 📋 Tabular alert list with timestamps and countries

---

 🧪 Sample Log Format

[2025-07-14 15:30:18] user=admin, ip=91.132.136.26, status=success

[2025-07-14 11:45:12] user=guest, ip=201.202.134.15, status=success

[2025-07-14 12:10:47] user=admin, ip=66.249.64.14, status=success

[2025-07-14 13:18:19] user=admin, ip=37.120.234.110, status=success

[2025-07-14 14:05:50] user=analyst, ip=190.92.153.34, status=success

[2025-07-14 14:45:32] user=root, ip=62.210.105.116, status=success

[2025-07-14 15:30:18] user=admin, ip=91.132.136.26, status=success

[2025-07-14 16:11:00] user=admin, ip=185.220.101.55, status=success

[2025-07-14 17:44:10] user=guest, ip=209.141.36.4, status=success

---

 ▶️ How to Run

1. Start the Geo Analyzer (backend processor)
   python geo_analyzer.py

2. Run the Flask Dashboard
   python app.py

Then open in browser:  
http://127.0.0.1:5001

---

 📸 Screenshots

<img width="1919" height="998" alt="3" src="https://github.com/user-attachments/assets/c0785bf1-8cc8-4248-a8e1-0f5725af3391" />
<img width="1920" height="1011" alt="2" src="https://github.com/user-attachments/assets/9e938fc7-6efc-4cb2-be77-19f811ea1086" />
<img width="1920" height="989" alt="1" src="https://github.com/user-attachments/assets/fc045f75-9bba-4118-bea2-fb87d4189a70" />


---

🔮 Ideas for Improvement

- Auto-refresh every 10 seconds  
- Add country flag emojis  
- WebSocket-based live updates  
- Email or SMS alerts for critical login anomalies

---

 🤝 Credits

Made by @Mrsanjai  
Day 07 of SOC Daily Log Extractor Series


---

 📌 License

MIT License – free to use with credit 🎓
