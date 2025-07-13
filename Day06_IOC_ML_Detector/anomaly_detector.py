# anomaly_detector.py

import os
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, min_samples=10):
        self.model = None
        self.min_samples = min_samples
        self.trained = False

    def train(self, log_file):
        if not os.path.exists(log_file):
            print(f"[ML] Training file not found: {log_file}")
            return

        with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
            lines = [line.strip() for line in f if line.strip()]

        X = [[len(line)] for line in lines]

        if len(X) < self.min_samples:
            print(f"[ML] Not enough samples to train: {len(X)}")
            return

        self.model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
        self.model.fit(X)
        self.trained = True
        print(f"[ML] Anomaly model trained on {len(X)} samples.")

    def is_anomalous(self, line):
        if not self.trained or self.model is None:
            return False
        X = [[len(line.strip())]]
        pred = self.model.predict(X)
        return pred[0] == -1
