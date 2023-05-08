# _*_coding :utf-8 _*_
# @Time :2022/5/21 12:54
# @File : 练习010-爬百度图片

import requests
import urllib.parse
import time
word = input('请输入关键词：')
# 该url只能获取html源码，源码中并没有图片的数据
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=000000&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=' + urllib.parse.quote(word)
print(url)
time.sleep(2)
response = requests.get(url)
content = response.text
print(content)











































