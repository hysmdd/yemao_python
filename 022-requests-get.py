# requests 网页采集
import requests

# 1. 指定url
# keyword = "张破虏"
keyword = input("请输入要查询的关键字：")
# url = "https://sogou.com/web?query={}".format(keyword)
url = f'https://sogou.com/web?query={keyword}'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
# 2. 网络请求，获得响应
resp = requests.get(url, headers=headers)
print(resp.text)

# 3. 下载并保存
with open(f'./file/{keyword}.html', 'w', encoding="utf-8") as f:
    f.write(resp.text)
    print(f"下载{keyword}.html文件完成")
