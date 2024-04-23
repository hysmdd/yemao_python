# xPath案例-下载人生格言
import requests
from lxml import etree
import re

base_url = "https://www.juzikong.com"
url = "https://www.juzikong.com/works/8d23eb5d-4e12-4d3b-b3cb-4b646ddfa005"
index_url = "https://www.juzikong.com/categories/works/books"

headers = {
    "Referer": "https://www.juzikong.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# resp = requests.get(url, headers=headers)
with open('./file/juzi.html', 'r', encoding='UTF-8') as f:
    text = f.read()

html = etree.HTML(text)
result = html.xpath('//li//div[@class="sentenceCard"]//div[@class="top"]//span[@class="link"]/text()')

for item in result:
    print(re.sub('  ', '', item))
    print("=" * 120)

with open('./file/打火机与公主裙经典语录.txt', 'w', encoding='UTF-8') as f:
    for item in result:
        f.writelines(re.sub('  ', '', item))
        f.writelines("\n\n")

index_resp = requests.get(index_url, headers=headers)
index_html = etree.HTML(index_resp.text)
urls = index_html.xpath('//div[@class="content_1fkvO"]//a/@href')
print("url批量提取完成")
for url in urls:
    url = base_url + url
    resp = requests.get(url, headers=headers)
    html = etree.HTML(resp.text)
    book_name = html.xpath('//title/text()')[0]
    print(f"准备下载{book_name}")
    result = html.xpath('//div[@class="sentenceCard"]//span/text()')
    with open(f"./file/{book_name}.txt", "w", encoding="UTF-8") as f:
        print(f"开始下载{book_name}")
        for res in result:
            f.writelines(res)
            f.writelines("\n\n")
        print(f"{book_name}下载完成\n\n")
