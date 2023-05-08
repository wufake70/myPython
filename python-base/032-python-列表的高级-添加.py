# _*_coding :utf-8 _*_
# @Time :2022/5/8 15:25
# @File : 032-python-列表的高级
# @Project : python-base

""" 列表的高级（即 增，删，改，查）
一，增加
1.append（追加）;在列表后面追加一个对象或数据
2.insert
3.extend
"""
# append 追加
food_list = ['铁锅炖大鹅', '酸菜五花肉']
food_list.append('小鸡炖蘑菇')
print(food_list)

# insert 插入；用法：insert（index，object）。index（为下标，索引）
food_list.insert(1, '西红柿炒鸡蛋')
# 结果为 ['铁锅炖大鹅', '西红柿炒鸡蛋', '酸菜五花肉', '小鸡炖蘑菇']
print(food_list)

# extend 继承；将一个列表中的数据逐一追加到新列表后
food2_list = ['马铃薯炒土豆']
food_list.extend(food2_list)
# 结果为 ['铁锅炖大鹅', '西红柿炒鸡蛋', '酸菜五花肉', '小鸡炖蘑菇', '马铃薯炒土豆']
print(food_list)





























