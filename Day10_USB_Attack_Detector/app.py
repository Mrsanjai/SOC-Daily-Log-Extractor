from flask import Flask, render_template, request
import os
from usb_attack_detector import detect_usb_anomalies

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'log'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    alerts = []
    if request.method == 'POST':
        if 'file' not in request.files:
            alerts = ["❌ No file part."]
        file = request.files['file']
        if file.filename == '':
            alerts = ["❌ No selected file."]
        elif file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'usb_log_sample.log')
            file.save(filepath)
            alerts = detect_usb_anomalies(filepath)
        else:
            alerts = ["❌ Invalid file type. Please upload a .log file."]
    return render_template('index.html', alerts=alerts)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
