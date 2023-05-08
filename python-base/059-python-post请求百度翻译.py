# _*_coding :utf-8 _*_
# @Time :2022/5/11 18:27
# @File : 059-python-post请求百度翻译
# @Project : python-base

import urllib.request
import urllib.parse
import re

url = 'https://fanyi.baidu.com/sug'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}

data = {
    'kw': "hero"
}

# post请求的参数，必须要进行编码
#
data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求的参数，是不会拼接在url的后面的，而是需要放在请求对象的参数中
request = urllib.request.Request(url, data, headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
import json
# 字符串==》json对象 ，反序列化

# find = re.compile(r"{'k':'hero', 'v':(.*?)}")
# content = re.findall(find, content)
content = json.loads(content)

print(content)

fp = open('file_storage/p_百度翻译.json', 'w', encoding='utf-8')
# 序列化，JSON对象转化为字符串，但此时写入文本的数据对中文不太友好,(即JSON中的汉字仍无法翻译）解决方法：在控制台中复制，文本中粘贴
content = json.dumps(content)

fp.write(content)
fp.close()

"""
post请求的总结: post请求方式的参数，必须编码   data = urllib.parse.urlencode(data).encode('utf-8')
 编码之后，必须调用encode方法
 参数是放在请求对象定制的方法中，
 request = urllib.request.Request(url=url, data=data, headers=headers)
"""




































