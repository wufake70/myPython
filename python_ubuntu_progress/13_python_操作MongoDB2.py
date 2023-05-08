# _*_coding :utf-8 _*_
# @Time :2022/8/4 20:44
# @File : python_操作MongoDB2
# @Project : python_ubuntu_progress

import pymongo
import pprint

# 利用 类去封装增删改查功能


class MyOperateMongoDB:
    def __init__(self, database, collection):           # 指定 数据库以及集合
        self.client = pymongo.MongoClient()             # 返回 一个链接的 mongo对象
        self.db = self.client[database]                 # 使用哪一个 数据库
        self.doc = self.db[collection]                  # 操作哪一个集合

    def insert(self, data, onlyOne = True):  #
        if onlyOne:
            self.doc.insert_one(data)
        else:
            self.doc.insert_many(data)

    def find(self, query=None, onlyOne = True):
        if onlyOne:
            ret = self.doc.find_one(query)
        else:
            ret = self.doc.find(query)
            ret = list(ret)
        return ret

    def update(self,condition, new_data, onlyOne=True):
        if onlyOne:
            self.doc.update_one(condition, new_data)
        else:
            self.doc.update_many(condition, new_data)

    def delete(self,condition,onlyOne=True):
        if onlyOne:
            self.doc.delete_one(condition)
        else:
            self.doc.delete_many(condition)


# 实例化一个对象
test = MyOperateMongoDB('test', 'test1')

print(test)
print(id(test))
print(test.doc.find())              # 返回一个游标对象
pprint.pprint(list(test.doc.find()))    # 转换为列表对象
print(isinstance(test,  MyOperateMongoDB))     # 判断是否 是实例化对象
print('='*60)

# 增加
# test.insert({'name': '明天你好', '类型': '歌曲'})  单条数据
# 多条数据 插入
# test.insert([{'name': 'Meizu17', 'brand': '魅族', 'CPU': '骁龙875'}, {'name': 'oppo A52', 'brand': 'oppo' , 'CPU': '骁龙666'}], onlyOne=False)

# 查询
# find_1 = test.find(onlyOne=False)         # 无条件查询多值
# find_1 = test.find({'name':'Meizu17'})    # 条件查询
# find_1 = test.find({'age': {'$gte': 9}}, onlyOne=False)  # 条件查询多值
# print(find_1)

# 改
# test.update({'brand': '魅族'}, {'$set': {'brand': 'Meizu'}})  单挑数据
# 多条数据
# test.update({},{'$set': {……}} ,onlyOne=False)

# 删除
# test.delete({'name': 'AD钙奶'})    # 单条数据
# 多条数据
# test.delete({'name': 'AD钙奶'}, onlyOne=False)    多行数据。






