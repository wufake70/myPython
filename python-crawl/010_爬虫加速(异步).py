# _*_coding :utf-8 _*_
# @Time :2022/10/14 15:29
# @File : 010_爬虫加速
# @Project : python-crawl

"""
1.  多进程
2.  多线程

3.  异步(在io密集型 使用异步 效率更高)

对比: 前两个 可理解为 多个人做 多件事情，
      后者 则是 一个人 做两件 事情。

4.  使用 异步网络库 aiohttp
"""
import aiohttp
import asyncio


async def download(url:str)->aiohttp.ClientResponse:
    # 初始化通信
    async with aiohttp.ClientSession() as session:
        # 构造函数 
        async with session.get(url) as res:
            # 发送请求并获取响应报文
            html_text = await res.text()    # await 标识这个操作需要等待的操作。

            print("wufake")
            return html_text
        # with 关键字 是为了自动断开链接。

loop = asyncio.get_event_loop()

# 执行单个任务
# loop.run_until_complete(asyncio.ensure_future(download('https://bj.newhouse.fang.com/house/s/b91/')))

# 执行多个任务
task_li = []
for page in range(1,39):
    src = "https://bj.newhouse.fang.com/house/s/b91/" + str(page)
    task = download(src)
    task_li.append(task)

loop.run_until_complete(asyncio.wait(task_li)) # 等到所有响应 全部返回才结束



















