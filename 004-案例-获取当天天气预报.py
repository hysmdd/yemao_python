# 获取天气预报
import requests
import json
import pprint

url = "https://api.openweathermap.org/data/2.5/weather?q=shenzhen&mode=json&units=metric&lang=zh_cn&APPID=83b30d525bff7db3e396e99abc62bd75"
resp = requests.get(url)
# print(resp.text)
resp_json = json.loads(resp.text)
# pprint.pprint(resp_json)

temp = resp_json['main']['temp']
city = resp_json['name']
weather = resp_json['weather'][0]['description']
print(f'【{city}】天气状况【{weather}】，温度【{temp}℃】')
