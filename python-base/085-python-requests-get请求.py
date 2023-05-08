# _*_coding :utf-8 _*_
# @Time :2022/5/21 11:19
# @File : 085-python-requests-get请求
# @Project : python-base

import requests

url = 'https://www.baidu.com/s?'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
           }
params = {

    'wd': '北京'
}

# url 请资源路径； params 参数； kwargs 字典；
response = requests.get(url=url, headers=headers, params=params)
content = response.content.decode('utf-8')
print(content)

# 总结：
# params（参数）使用params来传递
# params不需要urlencode编码
# requests不需要请求对象的定制
# 请求路径中的？可以删去
























