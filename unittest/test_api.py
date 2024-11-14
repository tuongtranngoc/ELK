import json

import requests


url = f'http://192.168.1.197:5000/send_data'

headers = {'Content-type': 'application/json', 'Authorization': 'Kalapa_123456789'}
data = json.load(open('data/messages/logs.json'))

res = requests.post(url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers).json()

print(res)
