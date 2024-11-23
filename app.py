from flask import Flask, request
from flask_cors import CORS
import requests
import os

from configs.elk_config import app_config


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

LOGSTASH_URL = f"http://{app_config.BASE_URL}:{os.getenv('LOGSTASH_PORT')}"

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.get_json()
    authorization_header = request.headers.get('Authorization', None)
    if isinstance(data, dict):
        data['user_id'] = authorization_header
        res = requests.post(LOGSTASH_URL, json=data)
        return {"status": "Success", "message": data}
    else:
        return {"status": "Error"}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=app_config.API_PORT, debug=True)
