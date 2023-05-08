# _*_coding :utf-8 _*_
# @Time :2022/5/18 18:15
# @File : 084-python-requests库基本使用
# @Project : python-base

import requests

url = 'https://www.baidu.com/'
response = requests.get(url)

# 一个类型和六个属性
# response类型
# <class 'requests.models.Response'>
# print(type(response))

# 1.encoding属性
# 设置相应的编码的格式
response.encoding = 'utf-8'

# url 返回一个url地址
# print(response.url)

# 3.content 返回二进制的数据
# print(response.content)

# 4.status_code 返回响应码
# print(response.status_code)

# 5.headers 返回相应的响应头
# print(response.headers)

# 6.text 以字符串的形式返回网页源码(最常用）
# print(response.text)
