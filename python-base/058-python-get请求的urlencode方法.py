# _*_coding :utf-8 _*_
# @Time :2022/5/11 17:56
# @File : 058-python-get请求的urlencode方法
# @Project : python-base

"""
# urlencode应用场景：url中多个参数
# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7


"""
import urllib.request
import urllib.parse
# 该方法可以减少拼接
# data = {
#     'wd': '周杰伦',
#     'sex': '男',
#     'location': '中国台湾'
# }
#
# a = urllib.parse.urlencode(data)
# print(a)

base_url = 'https://www.baidu.com/s?'
data = {
'wd': '周杰伦',
'sex': '男',
'location': '中国台湾'
}
data = urllib.parse.urlencode(data)
url = base_url + data
print(url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode()

print(content)





















































