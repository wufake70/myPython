# _*_coding :utf-8 _*_
# @Time :2022/10/14 10:27
# @File : 009_MongoDB
# @Project : python-crawl

"""

MongoDB:
    数据库 ---> 集合 ---> 文档 ---> 数据




"""

from pymongo import MongoClient

# 实例化对象
client = MongoClient("127.0.0.1", 27017)

# 创建(链接)一个数据库
d1 = client.db001           # 如果存在就直接链接 如果没有就会自动创建
test = d1.test              # 创建集合()

# 添加 单条数据
# test.insert_one({"test": "000", "name": "878424"})

# 添加多条数据
test.insert_many([{"test": "000", "name": "878424"}, {"test": "000", "name": "878424"}])







































