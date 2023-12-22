import requests
import json
import time


data = {}
currentTime = time.time()

with open('data.json', 'r', encoding='utf-8') as f:
    try:
        if 'timestamp' in json.load(f) and :
            with open('data.json', 'w', encoding='utf-8') as f:
                data = requests.get('https://poe.ninja/api/data/currencyoverview?league=Affliction&type=Currency')
                data = json.loads(data.text)
                data['timestamp'] = time.time()
                json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(e)


