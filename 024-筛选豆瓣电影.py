# 筛选豆瓣电影
import requests

url = "https://m.douban.com/rexxar/api/v2/movie/recommend"

tags = '犯罪'
excepted_rate = 8
page_size = 100

params = {
    'refresh': '0',
    'start': '0',
    'count': page_size,
    'uncollect': 'false',
    'tags': tags
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Referer': 'https://movie.douban.com/explore'
}

resp = requests.get(url, params=params, headers=headers)
result = resp.json()['items']
# print(result)

for item in result:
    if item['card'] == 'subject' and item['rating']['value'] > excepted_rate:
        print("*"*30)
        print(f"电影名称：{item['title']}")
        print(f"上映时间：{item['year']}")
        print(f"电影评分：{item['rating']['value']}")
        print(f"海报照片：{item['pic']['large']}")
