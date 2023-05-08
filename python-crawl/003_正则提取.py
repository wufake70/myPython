# _*_coding :utf-8 _*_
# @Time :2022/10/9 12:17
# @File : 003_正则提取
# @Project : python-crawl

import re

"""
1、re.match(pattern, string, flags)
    尝试从字符串其实位置 按照一个模式匹配，如果不是起始位匹配成功，就返回None
    
    pattern     匹配模式
    string      原字符串
    flags       用于控制正则表达式的匹配模式，如: 是否区分大小写、是否多行匹配
    
    flags 的参数
    re.I        对大小写不敏感
    re.M        多行匹配
    re.S        使 "." (通配符) 匹配的内容包括换行。
   
2、 re.search() 
    与match 相比，不局限起始位置，但只返回一个
    
3、 re.findall()
    返回一个列表
    
4、 re.sub(pattern, repl, string, count)
    可以把匹配到的内容 替换
    pattern     ....
    repl        要替换的字符串(他也可以是一个函数)
    string      原字符串
    count       替换次数
    
    
"""

# 使用正则 分别提取出 斜杆之间的 内容
a = 'https://ke.qq.com/webcourse/2929932/106040703#taid=13701899159909644&vid=387702306530086954'
b = re.findall('/{1,2}([^/]*)', a, re.S)


# /{1,2} 斜杆会出现一到两次
# ([^/]*) 将斜杆后的内容分组
# [^/]*  不匹配 斜杆  # 注意这里不能使用 "."通配符，因为它 包含了 斜杆。
# print(b)

# 定义 用于替换的函数
def fun(b):
    if 'qq.com' in b.group():  # 调用 group方法 才能获取 匹配到的内容。
        return '/www.baidu.com'  # 直接返回 字符串
    return b.group()


# 将斜杆之间的 字符 替换为 *号
# d = re.sub('/[^/]+', '/*', a, re.M)

d = re.sub('/[^/]+', fun, a, re.M)
print(d)
