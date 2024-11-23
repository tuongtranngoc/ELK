import sys
import json
import requests

sys.path.insert(0, ".")

from configs.elk_config import app_config

url = f'http://{app_config.BASE_URL}:{app_config.API_PORT}/send_data'
print(f"server url: {url}")
headers = {'Content-type': 'application/json', 'Authorization': '123456789'}
data = json.load(open('data/messages/logs.json'))
print(f"request data: {data}")

res = requests.post(url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers).json()

print(res)
