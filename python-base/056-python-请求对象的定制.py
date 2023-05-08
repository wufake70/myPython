# _*_coding :utf-8 _*_
# @Time :2022/5/10 13:55
# @File : 056-python-请求对象的定制
# @Project : python-base

import urllib.request
url = 'https://www.baidu.com'
"""
url的组成
例如： http://www.baidu.com/s?wd=周杰伦
http/https  www.baidu.com  80/443   s       wd =周杰伦    #
协议         主机（域名）  端口号   路径     参数         描点

协议  端口号
http   80
https   443
mysql   3306
oracle  1521
redis   6379
mongodb  27017
"""

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
# 因为urlopen方法中不能存储字典，所以headers不能传进去
# 需要请求对象的定制
# 注意：因为参数顺序问题，不能直接写在url和headers，
# 中间还有data参数，所以我们需要关键字传参
request = urllib.request.Request(url=url, headers=headers)


response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# 第一个反爬手段，用户代理（UA)
print(content)





























