from flask import Flask, jsonify, request
import requests


app = Flask(__name__)


@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.get_json()
    logstash_url = "http://localhost:5044"
    response = requests.post(logstash_url, json=data)
    return jsonify({"status": "Success"}), response.status_code


if __name__ == '__main__':
    app.run(port=5000, debug=True)