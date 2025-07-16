🧠 Day 9 – Time-Based Behavioral Anomaly Detector

This project detects unusual login behavior based on **time of access per user**.

🚀 Features
- Parses login timestamps
- Learns typical login hour ranges per user
- Flags logins outside the normal time range
- Outputs CSV + HTML-friendly data

📁 File Structure

Day09_Behavioral_Anomaly_Detector/

├── behavioral_analyzer.py

├── sample_user_logins.csv

├── output/

│ └── anomalies.csv

├── templates/

│ └── report.html

├── README.md

└── requirements.txt


📊 Output
An `anomalies.csv` file is generated with:
- Username
- Timestamp
- Normal login hour range
- Anomaly flag ✅ / ❌

 ▶️ How to Run

```bash
pip install -r requirements.txt
python behavioral_analyzer.py


---

✅ 5. `requirements.txt`

pandas

Screenshot:



---

By Sanjai.R,
LINKEDIN - www.linkedin.com/in/sanjai-r-60676126b

