import os

import requests
import json

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&mode=json&units=metric&lang=zh_cn&APPID=83b30d525bff7db3e396e99abc62bd75'
    resp = requests.get(url)
    resp_json = json.loads(resp.text)
    # pprint.pprint(resp_json)
    city_name = resp_json['name']
    temp = resp_json['main']['temp']
    temp_max = resp_json['main']['temp_max']
    temp_min = resp_json['main']['temp_min']
    weather = resp_json['weather'][0]['description']
    print(f"【{city_name}】今天天气【{weather}】，平均温度【{temp}℃ 】，最高温度【{temp_max}℃ 】，最低温度【{temp_min}℃ 】")


city_name = input('请输入城市的拼音：')
get_weather(city_name)
print("\n\n")
os.system("pause")
