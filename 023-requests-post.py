# 在线翻译
import requests

url = 'https://fanyi.sogou.com/reventondc/suggV3'

text = input("请输入要翻译的英文单词: ")

data = {
    'from': 'auto',
    'to': 'zh-CHS',
    'client': 'web',
    'text': f'{text}',
    'uuid': '4a29f1c7-4669-451d-b051-97bfee175818',
    'pid': 'sogou-dict-vr',
    'addSugg': 'on'
}

resp = requests.post(url, data=data)
result = resp.json()['sugg']
# pprint.pprint(result)

for item in result:
    print(">", item['v'])
