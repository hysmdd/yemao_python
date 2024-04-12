# 异常捕获
import requests
import json

# a = 1
# b = 0
# try:
#     c = a / b
# # except ZeroDivisionError as e:
# #     print("错误：被除数为0")
# #     print(e)
# # except NameError as e:
# #     print("错误：变量未定义")
# #     print(e)
# except:
#     print("出现错误")
# else:
#     print(f"{a} ÷ {b} = {c}")
# finally:
#     print("程序运行完毕")

url = f'https://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=83b30d525bff7db3e396e99abc62bd75'
try:
    resp = requests.get(url, timeout=2)
except:
    print("请求异常")
    resp = ''

if resp != '':
    resp_json = json.loads(resp.text)
    # pprint.pprint(resp_json)
    city_name = resp_json['name']
    temp = resp_json['main']['temp']
    temp_max = resp_json['main']['temp_max']
    temp_min = resp_json['main']['temp_min']
    weather = resp_json['weather'][0]['description']
    print(f"【{city_name}】今天天气【{weather}】，平均温度【{temp}℃】，最高温度【{temp_max}℃】，最低温度【{temp_min}℃】")
else:
    print("请求数据为空，无法解析")
