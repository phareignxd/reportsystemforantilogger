from flask import Flask, request, jsonify
import json
import os
import requests

app = Flask(__name__)

WEBHOOK_URL = 'https://discord.com/api/webhooks/1412408172093902888/1YCE9WLdHqOx7wgTll5_azX_zpKayaspLWR-8JzSf9NfNpkmHO4FXqa8DyzKHVtFQu4C'
REPORT_FILE = 'reports.json'

if not os.path.exists(REPORT_FILE):
    with open(REPORT_FILE, 'w') as f:
        json.dump([], f)

@app.route('/report1', methods=['POST'])
def report1():
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'message': 'No JSON provided'}), 400
    with open(REPORT_FILE, 'r') as f:
        reports = json.load(f)
    reports.insert(0, data)
    if len(reports) > 100:
        reports.pop()
    with open(REPORT_FILE, 'w') as f:
        json.dump(reports, f, indent=4)
    requests.post(WEBHOOK_URL, json=data)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
