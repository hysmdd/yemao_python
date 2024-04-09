# 使用API，获取重庆和北京的天气预报，包括平均温度，最低、最高温度，天气状况
# 打印这些城市的天气状况
import requests
import json
import pprint


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
    print(f"【{city_name}】今天天气【{weather}】，平均温度【{temp}℃】，最高温度【{temp_max}℃】，最低温度【{temp_min}℃】")


if __name__ == '__main__':
    # 获取重庆的天气情况
    get_weather('chongqing')
    # 获取北京的天气情况
    get_weather('beijing')


