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

bash
pip install -r requirements.txt
python behavioral_analyzer.py



✅ 5. `requirements.txt`

pandas

Screenshot:

<img width="1920" height="1023" alt="2" src="https://github.com/user-attachments/assets/7d65b64f-02a7-428d-9d06-e830be4677db" />
<img width="1920" height="1007" alt="1" src="https://github.com/user-attachments/assets/98393a86-edc6-4feb-b5c2-86875c742cb3" />


By Sanjai.R,
LINKEDIN - www.linkedin.com/in/sanjai-r-60676126b

