# 协程爬取图片
import asyncio
import aiohttp
import aiofiles
from bs4 import BeautifulSoup
from tqdm import tqdm
import math


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}


async def get_index_url(index_url, semaphore, i):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(index_url, headers=headers) as r:
                # print(await r.text())
                soup = BeautifulSoup(await r.text(), 'html.parser')
                a_list = soup.find('ul', class_="poster-col3").find_all('a')
                links = []
                for a in a_list:
                    link = a['href']
                    link = link.replace('#comments', '')
                    links.append(link)
        print(f"第{i + 1}页的链接提取完成")
        return links


async def get_hd_url(url, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as r:
                soup = BeautifulSoup(await r.text(), 'html.parser')
                link = soup.find('div', class_='photo-wp').find('img')['src']
                title = link.split('/')[-1].split('.')[0]
                print(f"已获取{title}地址，等待下载")
        return link, title


async def downloads(link, title, semaphore, tdm):
    async with semaphore:
        # print(f"正在下载{title}")
        async with aiohttp.ClientSession() as session:
            async with session.get(link, headers=headers) as r:
                async with aiofiles.open(fr'./file/images/点燃我温暖你/{title}.jpg', 'wb') as f:
                    await f.write(await r.content.read())
                    # print(f"{title}.jpg下载完成")
                    tdm.update(1)


async def main():
    semaphore = asyncio.Semaphore(3)

    task1 = []
    total_count = 68
    total_pages = math.ceil(total_count / 30)
    for i in range(0, total_pages):
        index_url = f'https://movie.douban.com/subject/35196753/photos?start={i * 30}'
        task1.append(asyncio.create_task(get_index_url(index_url, semaphore, i)))
    dones, peddings = await asyncio.wait(task1)

    task2 = []
    for done in dones:
        pages = done.result()
        for page in pages:
            task2.append(asyncio.create_task(get_hd_url(page, semaphore)))
    dones, peddings = await asyncio.wait(task2)

    task3 = []
    with tqdm(total=total_count) as tdm:
        for done in dones:
            link, title = done.result()
            task3.append(asyncio.create_task(downloads(link, title, semaphore, tdm)))
        await asyncio.wait(task3)


if __name__ == '__main__':
    asyncio.run(main())
