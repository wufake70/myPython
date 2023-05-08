# _*_coding :utf-8 _*_
# @Time :2022/10/9 21:54
# @File : 004_xpath
# @Project : python-crawl


"""
1.  lxml 是 Python的一个解析库，支持HTML和xml的解析，
    支持xpath解析方式，而且解析效率非常高。

    xpath 、xml的路径语言，他是一门在xml文档中查找信息的语言，
    他最初是用来查询xml文档的，但是他同样适用与html文档搜索。


2.  *                   通配任何节点
    @*                  通配任何属性
    /                   当前元素的子元素  (/) 表示根节点
    //                  当前元素的后代
    .                   当前元素 (/.)
    ..                  当前元素的 父元素 (/..)
    @属性名             获取当前元素的某个属性的属性值
    nodename            通过节点名称
    nodename[@属性名="属性值"]    通过 标签的属性来查找   (也可以使用不等于 !=)('//div[@id="react-body"]')
    nodename[@class="①... ②..."]  可以写入 多个类属性值
    [数字]                索引取元素
    [last()]             最后一个...元素
    [last()- 1]          倒数第二个...元素
    [position() <= 3]    位置小于3 的元素(即前3个元素)  ('//div[@class="table-box"][position()<=3]')
    //nodename[@..][@..]    多个属性判断

3.  text()              获取当前元素文本内容  (/text())
    contains()          获取某个元素属性 包含 某个属性值的元素  ('//div[contains(@class, "clearfix")]')
    startswith()        .....   ('//div[contains(@class, "clearfix")]')


4.   from lxml import etree
     element = etree.HTML(html_text)
     element.xpath('.....')

"""
# from lxml import etree
#
# a = "<a src='www.some.com'><span>hello </span>world</a>"
#
# html = etree.HTML(a)
# print(html.xpath('//a//@src'))
import re

b = 'hel\tlo wo\nrld'


# print(re.findall('\s', b, re.M))
# print(re.sub('\s', '', b, re.M))

li = ['a;\ndk;', 'fpu\ti', 'kfjq\te\nw', 'poie\th\nj', 'pif\t uq\nei']

print(','.join(li))
ls = []
for i in li:
    print(li.index(i))
    ls.append(re.sub('[\n\t]', '', i, re.M))

print(ls)
