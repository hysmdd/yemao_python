import asyncio
import aiohttp
import aiofiles
import requests

url_list = [
    'https://img1.doubanio.com/view/photo/l/public/p2883210228.jpg',
    'https://img9.doubanio.com/view/photo/l/public/p2883127824.jpg',
    'https://img1.doubanio.com/view/photo/l/public/p2883210229.jpg'
]


async def downloads(url):
    file_name = url.split("/")[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            # with open(fr'./file/images/{file_name}', 'wb') as f:
            #     f.write(await r.content.read())
            #     print(f"{file_name}下载完成")
            async with aiofiles.open(fr"./file/images/{file_name}", "wb") as f:
                await f.write(await r.content.read())
                print(f"{file_name}下载完成")


async def main():
    tasks = []
    for url in url_list:
        tasks.append(asyncio.create_task(downloads(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
