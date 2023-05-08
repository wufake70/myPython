# _*_coding :utf-8 _*_
# @Time :2022/5/9 16:49
# @File : 041-python-字典高级-删除
# @Project : python-base

"""
删除
   del
   1.用法一，del 变量['元素名’]   删除字典中一个指定的元素
   2.用法二，del 变量    直接删除整个字典

   clear 清空：将字典中所有的元素都清空，但保留原变量
    用法：变量命.clear
"""
person = {'name': '老马', 'age': '33'}

# del
del person['age']
# 结果为
print(person)
del person
# print(person)，del 已删除person变量，print会报错

person1 = {'name': '老马', 'age': '33'}
person1.clear()
# 结果为 {}
print(person1)


















































