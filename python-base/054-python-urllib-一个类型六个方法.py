# _*_coding :utf-8 _*_
# @Time :2022/5/10 11:27
# @File : 054-python-urllib-一个类型六个方法
# @Project : python-base

import urllib.request

url = 'http://www.baibu.com'

# 模拟浏览器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# 一个类型 <class 'http.client.HTTPResponse'>
print(type(response))

# read()按照一个一个字节读取(效率慢）
# read（数字）读取多少字节
# content = response.read()
# print(content)

# readline() 只读一行
# readlines（）读取全部（效率高）
# decode（）方法只能先读取在解码
content = response.readlines()
print(len(str(content)))

# getcode()返回状态码,返回200，即成功
print(response.getcode())

# getheaders(),获取状态信息
print(response.getheaders())































