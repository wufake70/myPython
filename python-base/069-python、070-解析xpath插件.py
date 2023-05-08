# _*_coding :utf-8 _*_
# @Time :2022/5/13 17:03
# @File : 069-python-解析xpath插件
# @Project : python-base

from lxml import etree
# 导入相关的库需要pip指令来完成

# 解析常用
# 1.xpath     能够获取网页源码中部分源码的一种方式
# 2.jsonpath
# 3.beautifulsoup


# xpath解析两种文件
# 1.本地文件（html的部分数据）
# 对应方法：etree.parse

# 2.服务器响应的数据 response.read().decode('')（应用最多）
# 对应方法：etree.HTML()



# 一，xpath解析本地文件
tree = etree.parse('051-python-网页的结构介绍.html')
# xpath解析严格遵守html代码规范，标签必须完整
# print(tree)

# 1.路径查询：tree.xpath('xpath路径') ,路径写对了想啥要啥
# 查找ul下面的li，xpath的语法规则：一个‘/'是找它的儿子元素，
# 两个’/'（//)是找它的子孙后代元素。
# text()方法可以获取标签中的内容
li_list = tree.xpath('//body//li/text()')
print(li_list)
# 判断列表的长度
print(len(li_list))

# 查找的所有的id属性的li标签,语法：  .../标签名[@属性名] .注意：id属性独有
li_list = tree.xpath('//body//li[@id="a"]/text()')
print(li_list)

# 属性查询（id也是属性），语法：  ..../标签名[@属性名]
li_list = tree.xpath('//body//li[@class="b"]/text()')
print(li_list)

# 内容查询， 语法： .../text()


























