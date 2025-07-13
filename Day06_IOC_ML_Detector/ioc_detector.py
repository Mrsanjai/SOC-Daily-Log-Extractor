# ioc_detector.py

import time
from datetime import datetime

IOC_KEYWORDS = {
    "mimikatz":   ("Credential Access", "T1003.001", "high"),
    "powershell": ("Execution",         "T1059.001", "medium"),
    "net user":   ("Discovery",         "T1087.001", "medium"),
    "rundll32":   ("Execution",         "T1218.011", "high"),
    "cmd.exe":    ("Execution",         "T1059.003", "medium"),
    "ftp":        ("Command & Control", "T1105",     "high"),
    "curl":       ("Command & Control", "T1105",     "medium"),
    "nmap":       ("Reconnaissance",    "T1046",     "medium")
}

def detect_ioc(line):
    for keyword, (tactic, technique, severity) in IOC_KEYWORDS.items():
        if keyword.lower() in line.lower():
            alert = {
                "id": f"ioc-{int(time.time())}",
                "source": "IOCDetector",
                "ioc": keyword,
                "timestamp": datetime.utcnow().isoformat(),
                "summary": f"⚠️ Detected '{keyword}' in log stream",
                "status": "new",
                "severity": severity,
                "mitre_tactic": tactic,
                "mitre_technique": technique
            }
            return alert
    return None
