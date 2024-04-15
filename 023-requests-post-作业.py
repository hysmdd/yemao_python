# 基于百度翻译，实现文本翻译
import requests

url = "https://fanyi.baidu.com/sug"

keyword = input("请输入要翻译的单词: ")

data = {
    'kw': keyword
}

resp = requests.post(url, data=data)
result = resp.json()['data']
for item in result:
    print(">", item['k'], ":", item['v'])
