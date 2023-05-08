# _*_coding :utf-8 _*_
# @Time :2022/10/12 10:15
# @File : 测试2
# @Project : python-crawl


import requests


url = "https://www.vcg.com/creative/3287/"

res = requests.get(url)

print(res.text)

















