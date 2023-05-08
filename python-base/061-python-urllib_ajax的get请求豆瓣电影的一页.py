# _*_coding :utf-8 _*_
# @Time :2022/5/11 21:38
# @File : 061-python-urllib_ajax的get请求豆瓣电影的一页
# @Project : python-base

# 获取豆瓣电影第一页的电影
import urllib.request
import urllib.parse
import json

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
           }

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

# 数据下载到本地文件
# open方法默认情况下使用的是gbk的编码，如果我们要想保存汉字
# 那么需要在open方法中指定编码格式为utf-8
fp = open('file_storage/豆瓣电影.json', 'w', encoding='utf-8')
fp.write(content)
fp.close()

























