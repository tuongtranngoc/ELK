from flask import Flask, request
import requests


app = Flask(__name__)
LOGSTASH_URL = "http://192.168.1.197:5045"


@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.get_json()
    authorization_header = request.headers.get('Authorization', None)
    if isinstance(data, dict):
        data['user_id'] = authorization_header
    res = requests.post(LOGSTASH_URL, json=data)
    return {"status": "Success"}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
