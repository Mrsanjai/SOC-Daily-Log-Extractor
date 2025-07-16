
📶 Day 8 – IP Frequency Heatmap: Suspicious Repetition Detector

This mini SOC project visualises the frequency of IP addresses in a given log file and highlights repeated IPs that may signal malicious behaviour such as brute-force attacks, scanning, or beaconing.

🔍 Suspicious IP repetition is a common early-stage indicator in threat hunting and SOC operations. This tool gives you immediate visibility into IP frequency patterns.

🔥 Features

- 📊 Bar chart visualisation of top IP addresses by frequency
- ⚠️ Risk level tagging (Low, Medium, High) based on frequency thresholds
- 💡 Clean, modern Cyber Dark UI with animated cards
- 🧠 Real-world SOC relevance: quickly identify attackers reusing the same IPs
- 📝 Uses sample alerts.json or can be modified for dynamic uploads

🖥️ Dashboard Preview

[Insert Screenshot Here]

🚀 Getting Started

1. Clone the repository

git clone https://github.com/Mrsanjai/SOC-Daily-Log-Extractor.git
cd SOC-Daily-Log-Extractor/Day08_IP_Frequency_Heatmap

2. Install dependencies

pip install -r requirements.txt

3. Run the Flask app

python app.py

Then open your browser and visit:
http://127.0.0.1:5000/

📁 Project Structure

Day08_IP_Frequency_Heatmap/
├── app.py
├── templates/
│   └── dashboard.html
├── static/
├── data/
│   └── alerts.json
└── requirements.txt

📄 Sample Log Format (alerts.json)

[
  { "timestamp": "2025-07-15", "ip": "192.168.1.10", "message": "Login failed" },
  { "timestamp": "2025-07-15", "ip": "185.103.196.254", "message": "Port scan" }
]
<img width="1917" height="1009" alt="2" src="https://github.com/user-attachments/assets/85cb4733-f3a1-4eb9-96a4-3194b96324da" />

<img width="1920" height="982" alt="1" src="https://github.com/user-attachments/assets/d3d0bb15-de8b-4c80-af5c-bc33bcf177c4" />

✔️ Tool automatically extracts and counts all valid IPs.

📌 Risk Thresholds

| Frequency | Risk Level | Color |
|-----------|------------|-------|
| >10       | 🔴 High     | Red   |
| 6–10      | 🟠 Medium   | Orange|
| 1–5       | 🟢 Low      | Green |

🙌 Built With

- Python
- Flask
- Chart.js
- Custom Cyber Dark UI (no Bootstrap)

📢 Author

Made with ❤️ by Sanjai R (https://github.com/Mrsanjai)  
This is part of my SOC Analyst Job Attack Mode – 6 Month Execution Plan

⭐ Show your support!

If this helped or inspired you, please:

- ⭐ Star the repo
- 🔁 Share on LinkedIn with #CyberSecurity #SOC #MiniSIEM
- 💬 Give feedback or suggest ideas

Stay consistent. Build daily. Dominate the SOC job market. 💪
