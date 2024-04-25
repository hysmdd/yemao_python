# 多线程下载小说
import os
import threading
import requests
from lxml import etree
from queue import Queue

gen_urls_done = False
book_name = ''
path = r'./file/books/'


def get_urls(index_url, download_queue):
    global gen_urls_done, book_name, path
    resp = requests.get(index_url)
    resp.encoding = "UTF-8"
    html = etree.HTML(resp.text)
    links = html.xpath('//ul[@class="list clearfix"]//li[@class="mulu"]//a/@href')
    book_name = html.xpath('//h1[@class="article-title"]/text()')[0]
    path += book_name
    if not os.path.exists(path):
        os.mkdir(path)
    # titles = html.xpath('//ul[@class="list clearfix"]//li[@class="mulu"]//a//text()')
    for link in links:
        download_queue.put(link)
    gen_urls_done = True
    print("地址解析完成，等待下载")


def downloads(download_queue):
    while True:
        if download_queue.empty() and gen_urls_done:
            print("已全部下载完成")
            break
        else:
            url = download_queue.get()
            resp = requests.get(url)
            resp.encoding = "UTF-8"
            html = etree.HTML(resp.text)
            content = html.xpath('//article[@class="article-content"]//p/text()')
            content = "".join(content).strip().replace("\u3000\u3000", "\n")
            title = html.xpath('//h1[@class="article-title"]/text()')[0]
            print(f"{threading.current_thread().name}开始下载{title}")
            with open(f"{path}/{title}.txt", 'w', encoding='UTF-8') as f:
                f.write(content + "\n\n")
                print(f"{threading.current_thread().name}已完成{title}下载")
                print("=" * 50)


def main():
    # index_url = 'https://www.52shuku.vip/xiandaidushi/3194.html'
    index_url = 'https://www.52shuku.vip/yanqing/12037.html'
    download_queue = Queue(maxsize=2000)
    th1 = threading.Thread(target=get_urls, args=(index_url, download_queue))
    th1.start()

    for i in range(3):
        th2 = threading.Thread(target=downloads, args=(download_queue,), name=f"线程{i}")
        th2.start()


if __name__ == '__main__':
    main()
