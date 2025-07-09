# 🔍 Day 2 – Log Alert Generator V1

A simple Python-based tool that scans system log files and detects suspicious activity based on predefined keywords. Designed as part of the SOC (Security Operations Center) Job Attack Mode to build real-world log analysis skills.

---

## 📂 Project Structure

Day02_LogAlertGenerator_V1/
├── log_alert_generator_v1.py # Main Python script
├── system.log # Sample input file with system logs
├── alerts_output.txt # Output: suspicious activity alerts
├── day2_code_showcase.html # HTML showcase of project with input/output/code
└── README.md # You’re reading this!


---

## 🚀 How It Works

The script reads each line of a system log file and checks for specific suspicious keywords such as:

- `Failed password`
- `Unauthorized`
- `Invalid user`
- `root login`

If a line contains any of these, it is tagged as an alert and written to an output file.

---

## 🛠️ How to Run

1. Make sure you have Python 3 installed.

2. Clone or download this project folder.

3. Inside the folder, make sure you have a `system.log` file (you can use the sample included).

4. Run the script:

```bash
python log_alert_generator_v1.py

Sample Input:
Jul 9 08:22:35 server sshd[12345]: Failed password for invalid user root from 192.168.1.100
Jul 9 08:22:37 server sshd[12346]: Accepted password for admin from 192.168.1.101
Jul 9 08:22:40 server sshd[12347]: Unauthorized access attempt from 192.168.1.105

Sample Output
[ALERT] Suspicious activity detected: Jul 9 08:22:35 server sshd[12345]: Failed password...
[ALERT] Suspicious activity detected: Jul 9 08:22:40 server sshd[12347]: Unauthorized access...

Author
Sanjai R.
Built as part of the 6-Month SOC Job Attack Mode
📅 Day 2 of 180 – Daily SOC Mini Projects

