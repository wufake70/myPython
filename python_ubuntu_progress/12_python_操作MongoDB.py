# _*_coding :utf-8 _*_
# @Time :2022/8/1 14:40
# @File : python_操作MongoDB
# @Project : python_ubuntu_progress
import pprint
import pymongo

# 连接 MongoDB
client = pymongo.MongoClient()

# 选择 要使用数据库
db = client['test']

# 选择 要操作的集合
collection = db['test1']

# 查看 文档数据
document = collection.find()
# print(document)             # 返回MongoDB 游标对象,无法查看相关文档数据
document = list(document)   # 将游标对象 转换 列表 即可
# pprint.pprint(document)

# 取出 一个集合 所有文档的 所有的 键值对
"""
for a in document:
    for i, j in a.items():              # 对于 字典取值操作
        print(f'{i}:{j}', end=',')
    print('')
"""

# ##增加数据
# 增加一条数据
# collection.insert_one({'name': '抢手蚊香','message': '无烟，大盘，有效驱蚊。'})

# 多条数据
# collection.insert_many([{'name': 'AD钙奶', 'brand': '娃哈哈', 'message': '蛋白质，脂肪，碳水化合物，维A。'}, {'name': '活动铅笔', 'brand': '得力', 'message': '直径0.7mm'}])

# 查找 条件过滤               (find()方法 需要转类型、列表、元祖
# new_data = collection.find({'age': {'$gt': 1}})  # 过滤出 age大于 1的数据.

# find_one() 只查找一条数据，不用转类型
# new_data = collection.find_one({'age': {'$gt': 1}})

# 注意: 所有的 键名都要 加引号
# new_data = list(new_data)
# print(new_data)


# ##修改 文档数据
# 修改 一条数据
# collection.update_one({'name': 'AD钙奶'}, {'$set': {'message': '信息不够准确！！'}})

# 全文档数据 替换
# collection._update_retryable({'name': 'AD钙奶'}, {'name': 'AD钙奶', 'message': '信息不够准确！！'})

# 修改 多条数据
# collection.update_many(……)

# ##删除 文档数据
# collection.delete_one({'name': '抢手蚊香'})   删除单条
# collection.delete_many()                      删除多条
































