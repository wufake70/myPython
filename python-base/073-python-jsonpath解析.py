# _*_coding :utf-8 _*_
# @Time :2022/5/14 17:47
# @File : 073-python-jsonpath解析
# @Project : python-base


import json
import jsonpath

# 把文件加载出来
obj = json.load(open('file_storage/store.json', 'r', encoding='utf-8'))

# 书店所有的书的作者
# 返回的数据类型为列表类型：
# author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')[1]
# print(author_list)

# 获取所有的作者
# author_lisdt = jsonpath.jsonpath(obj, '$..author')
# print(author_lisdt)

# 获取所有的store下的元素
# tag_list = jsonpath.jsonpath(obj, '$.store.*')
# print(tag_list)

# store下面的所有的钱
# money_list = jsonpath.jsonpath(obj, '$.store..price')
# print(money_list)

# 最后一本书
# book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# print(book)

# 前两本书
# book = jsonpath.jsonpath(obj, '$..book[0,1]')
# book = jsonpath.jsonpath(obj, '$..[:2]')
# print(book)

# 条件过滤，需要在（）前面添加一个
# 过滤出所有的包括isbn的书
# book = jsonpath.jsonpath(obj, '$..book[?(@.isbn)')
# print(book)

# 那本书超过了十块钱
book = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print(book)





















