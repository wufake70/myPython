# _*_coding :utf-8 _*_
# @Time :2022/5/10 11:06
# @File : 053-python-urllib库的基本使用
# @Project : python-base

"""
一，使用urllib来获取百度首页的源码
"""
# 1.定义一个url
url = 'http://www.baidu.com'
# 2.模拟浏览器向服务器发送请求
# 导入urllib.request
import urllib.request
response = urllib.request.urlopen(url)
# 3.获取响应中网页页面的源码
# read方法，返回的是字节类型的二进制数据
content = response.read()
# 我们要将二进制的数据转换为字符串 （该过程叫解码）
# 二进制==》字符串   方法：decode（'解码的格式'）
content = content.decode('utf-8')
# 4.打印数据
print(content)

fp = open('file_storage/baidu.txt', 'w')
fp.write(content)
fp.close()






























