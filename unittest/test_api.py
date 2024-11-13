import json

import requests


url = f'http://localhost:5000/send_data'

headers = {'Content-type': 'application/json'}
data = json.load(open('data/messages/logs.json'))

res = requests.post(url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers)