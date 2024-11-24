import sys
import json
import requests
import unittest

sys.path.insert(0, ".")

from configs.elk_config import app_config


class Test_API(unittest.TestCase):
    def test_api_post(self):
        url = f'http://{app_config.BASE_URL}:{app_config.API_PORT}/send_data'
        print(f"server url: {url}")
        headers = {'Content-type': 'application/json', 'Authorization': '123456789'}
        data = json.load(open('data/messages/logs.json'))
        res = requests.post(url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers).json()
        assert(isinstance(res['message']['user_id'], str))
    
    def test_api_not_authen(self):
        url = f'http://{app_config.BASE_URL}:{app_config.API_PORT}/send_data'
        print(f"server url: {url}")
        headers = {'Content-type': 'application/json'}
        data = json.load(open('data/messages/logs.json'))
        res = requests.post(url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers).json()
        assert(not isinstance(res['message']['user_id'], str))

if __name__ == "__main__":
    unittest.main()
