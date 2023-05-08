# _*_coding :utf-8 _*_
# @Time :2022/10/10 10:35
# @File : 005_BeautifulSoup
# @Project : python-crawl

from bs4 import BeautifulSoup
import lxml


a = """
<!DOCTYPE html>
<html>
 
<head>
<meta content="text/html;charset=utf-8" http-equiv="content-type" />
<meta content="IE=Edge" http-equiv="X-UA-Compatible" />
<meta content="always" name="referrer" />
<link href="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css" rel="stylesheet" type="text/css" />
<title>百度一下，你就知道 </title>
</head>
 
<body link="#0000cc">
<div id="wrapper">
<div id="head">
<div class="head_wrapper">
<div id="u1">
<a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻 </a>
<a class="mnav" href="https://www.hao123.com" name="tj_trhao123">hao123 </a>
<a class="mnav" href="http://map.baidu.com" name="tj_trmap">地图 </a>
<a class="mnav" href="http://v.baidu.com" name="tj_trvideo">视频 </a>
<a class="mnav" href="http://tieba.baidu.com" name="tj_trtieba">贴吧 </a>
<a class="bri" href="//www.baidu.com/more/" name="tj_briicon" style="display: block;">更多产品 </a>
</div>
</div>
</div>
</div>
</body>
"""

# 解析 html(实例化对象)
bs = BeautifulSoup(a, 'lxml')

# 查看 BeautifulSoup的 书型盒方法
# for i in dir(bs):
#     print(i)
"""
1、 bs.title            获取 文档 title标签
    bs.text             获取 整个文档文字内容
    bs.string           获取 整个文档的 字符串对象(可以使用 字符串的方法)
    string.replace_with()  将文档 中某些元素的字符 进行替换
    bs.tag              获取 文档某个 标签(但只能获取第一个)
    attrs               获取 元素的全部属性(以字典形式 返回)

2、 使用 css选择器 规则
    bs.select('css 选择器')
    bs.select('a')                          获取全部 a标签
    bs.select('a:contains("新闻")')         文本内容选择器(不推荐使用)
    bs.select('a:-soup-contains("新闻")')   文本内容选择器(推荐使用)
    
"""

# b = bs.select('a:contains("新闻")')
# bs.title.string.replace_with('000000')
print(bs)





























