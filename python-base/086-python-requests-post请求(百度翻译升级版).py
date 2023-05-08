# _*_coding :utf-8 _*_
# @Time :2022/5/21 16:13
# @File : 086-python-requests-post请求
# @Project : python-base

import requests
import json
import re

def fanyi():
    kw = input('请输入您想要查询的词：')
    url = 'https://fanyi.baidu.com/sug'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
               }
    params = {
        'kw': kw,
    }

    # 注意：post请求中参数是data（不是params）
    response = requests.post(url, data=params, headers=headers)
    content = response.text
    # post请求 返回的是字符串，但它是unicode字符集编码（对中文不要好），需要将其  Unicode ==》中文。（utf-8是编码规则）
    # print(content)
    # print(type(content))
    # 使用 json.loads 实现 Unicode ==》中文
    content = json.loads(content)
    # 经过json.loads加载过后变为字典类性
    # print(type(content))

    # 我们想要的数据，这里主要是content中的 data条目 (items) 中的值
    content = content.get('data')

    # 编写一个正则表达式的规则，注意：该规则只对str有效
    content = str(content)
    rule = re.compile(r"'(.*?)': '(.*?)'")
    result = re.findall(rule, content)
    # re.findall() 返回的是列表类型
    # print(content)

    # 将翻译内容输出
    # a = '%skw %s' % ('有关', '词义有：') 注意：转义字符 %s 的使用是为了减少拼串，已经拼串的时候就不能使用 %s
    print('有关' + kw + '的词义有：')
    for i in range(len(result)):
        print(result[i])
    print('感谢您的使用！！！')

for i in range(0, 11111):
    fanyi()






































