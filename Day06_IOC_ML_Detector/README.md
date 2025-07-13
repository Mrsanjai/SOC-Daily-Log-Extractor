
```markdown
# 🚨 Day 06 – IOC + ML-Based Real-Time Log Anomaly Detector

This project is a **real-time cybersecurity detection tool** that monitors **Sysmon logs** for suspicious activity using:

- 🔍 **IOC-based detection** (e.g., powershell, mimikatz, nmap)
- 🤖 **ML-based anomaly detection** using Isolation Forest
- 🧠 Continuous log monitoring and alert generation
- 📂 Alerts stored in `alerts.json` for UI or API consumption

---

## 📁 Project Structure

```

Day06\_IOC\_ML\_Detector/
├── main.py                    ← Real-time monitor (IOC + ML)
├── ioc\_detector.py           ← IOC keyword detection logic
├── anomaly\_detector.py       ← Machine Learning model
├── utils.py                  ← Alert saving and helpers
├── alerts.json               ← All generated alerts stored here
├── logs/
│   └── sysmon\_live.log       ← Live Sysmon export file
├── webapp/
│   ├── app.py                ← Flask web UI (optional)
│   ├── templates/
│   │   └── dashboard.html
│   └── static/
│       ├── style.css
│       └── js/
│           └── refresh.js
├── sysmon\_export.ps1         ← PowerShell: Exports Sysmon logs
└── README.md                 ← You're here!

````

---

## 🔧 How It Works

1. **Sysmon Export:**
   - A PowerShell script continuously extracts logs from `Microsoft-Windows-Sysmon/Operational`.
   - Appends output to `logs/sysmon_live.log`.

2. **Real-Time Monitoring:**
   - `main.py` tails the log file and checks every new line.
   - Runs both **IOC matchers** and **ML anomaly detector**.

3. **Alerts:**
   - Every detection is stored in `alerts.json`.
   - Alerts include MITRE Tactic, Technique, Severity, and Timestamp.

4. **UI Integration:**
   - The `webapp/` folder can render alerts visually via Flask (optional showcase).

---

## 🚀 Run the System

### Step 1 – Start Sysmon Export (in PowerShell)
```powershell
powershell -ExecutionPolicy Bypass -File sysmon_export.ps1
````

### Step 2 – Start the IOC + ML Detector

```bash
python main.py
```

> ✅ New lines in `sysmon_live.log` will be auto-scanned.
> ✅ Alerts will appear on the terminal + saved to `alerts.json`.

---

## 🧠 IOC Keywords Used

| Keyword    | Tactic            | Technique | Severity |
| ---------- | ----------------- | --------- | -------- |
| powershell | Execution         | T1059.001 | medium   |
| mimikatz   | Credential Access | T1003.001 | high     |
| net user   | Discovery         | T1087.001 | medium   |
| rundll32   | Execution         | T1218.011 | high     |
| cmd.exe    | Execution         | T1059.003 | medium   |
| ftp        | Command & Control | T1105     | high     |
| curl       | Command & Control | T1105     | medium   |
| nmap       | Reconnaissance    | T1046     | medium   |

---

## 🧠 ML Model Used

* **Isolation Forest**
* Features based on **log line length**
* Trained on initial logs in `sysmon_live.log`

> If insufficient data, ML detection is skipped.

---

## 📌 Sample Output

```plaintext
[*] Starting IOC + ML Detector...
[DEBUG] powershell.exe -EncodedCommand ...
[IOC ALERT] ⚠️ Detected 'powershell' in log stream
[ML ALERT] 🤖 ML anomaly detected: suspicious base64 command detected...
```

---

## 💡 Future Enhancements

* 🧠 NLP-based log content classification
* 📊 Dashboard with charts (using Chart.js or Dash)
* 🔗 REST API for integration with SIEM/SOAR
* 📲 Slack / Email / Telegram Alerting

---

## 📚 Credits

* Developed by: **Sanjai R**
* Project Day: **Day 06 – SOC Job Attack Mode**
* Stack: Python, Sklearn, Flask, Sysmon, PowerShell

---

> 🔐 Built as part of a CyberSOC Real-Time Detection Lab — simulates real enterprise monitoring environments.

```
