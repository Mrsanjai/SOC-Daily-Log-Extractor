from flask import Flask, render_template
import pandas as pd
from behavioral_analyzer import detect_anomalies

app = Flask(__name__)

@app.route('/')
def home():
    detect_anomalies("sample_user_logins.csv", "output")  # Always fresh
    df = pd.read_csv("output/anomalies.csv")
    data = df.to_dict(orient='records')
    return render_template("report.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
