# _*_coding :utf-8 _*_
# @Time :2022/5/12 22:26
# @File : 066-python-urllib_handler处理器的基本使用
# @Project : python-base

# 需求：使用handler来访问百度，获取网页源码
import urllib.request

url = 'http://www.baidu.com'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
          }

request = urllib.request.Request(url=url, headers=headers)

# handler   build_opener     ,open
# 1. 获取handler对象
handler = urllib.request.HTTPHandler()
# 2.获取opener对象
opener = urllib.request.build_opener(handler)
# 3.使用open方法
response = opener.open(request)
content = response.read().decode('utf-8')
print(content)
































