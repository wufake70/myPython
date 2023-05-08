# _*_coding :utf-8 _*_
# @Time :2022/5/11 17:23
# @File : 057-python-get请求的quote方法
# @Project : python-base

"""
拓展：
    编码集的演变：
        https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
        %E5%91%A8%E6%9D%B0%E4%BC%A6（Unicode编码） = 周杰伦
"""
import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd='
# 将周杰伦转为Unicode编码
name = urllib.parse.quote('周杰伦')
url = url + name
print(url)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)


































