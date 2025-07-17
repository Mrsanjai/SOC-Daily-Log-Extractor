🛡️ Day 10 – USB Attack Detector (Web-Based Mini SOC Project)

📌 Project Description
A Python + Flask-based SOC detection tool that scans USB activity logs for suspicious device insertions and off-hour access patterns.

Designed to simulate endpoint defense against **Rubber Ducky**, **MalDuino**, and other **HID spoofing attacks** using real-world tactics.

🚀 Features
- 🖥 Upload `.log` file via web UI
- ⚠ Detect unauthorized USB insertions (based on VID/PID)
- ⏰ Flag activity outside business hours (9 AM – 7 PM)
- 📂 Log alerts to `alerts_output.txt`
- 🎨 Clean Soft UI dashboard
- ✅ Real-time scan results on screen

📁 Project Structure

Day10_USB_Attack_Detector/

├── app.py

├── usb_attack_detector.py

├── suspicious_usb_devices.json

├── uploads/

│ └── usb_log_sample.log

├── templates/

│ └── index.html

└── static/

└── style.css (optional)


🧪 Sample Alert Output

⚠️ 2025-07-16 03:15:42: Suspicious device detected (Rubber Ducky) by admin - VID:0BAD, PID:C0DE
⏰ 2025-07-16 02:03:11: USB inserted outside business hours by attacker - Device: MalDuino



💡 Technologies Used
- Python 3
- Flask
- HTML/CSS (Soft UI Style)
- Jinja2
- Sysmon-style log simulation

📸 UI Preview

🧠 Ideal For
- SOC Analyst portfolio projects
- SIEM & endpoint detection practice
- Cybersecurity interview preparation

📦 How to Run
```bash
pip install flask
python app.py

Then open http://127.0.0.1:5000

By Sanjai.R
