# _*_coding :utf-8 _*_
# @Time :2022/5/9 17:01
# @File : 042-python-字典的遍历
# @Project : python-base

# 所谓遍历 就是将数据一个一个的输出

# 遍历字典的key
person = {'name': '老马', 'age': '22', 'sex': '男'}
# i为变量的名字，没有要求
for i in person:
    print(i)


# 遍历字典中的value
for i in person.values():
    print(i)


# 遍历字典中的key 和 value
for i, j in person.items():
    print(i, j)

# 遍历字典中的元素(项目）
for i in person.items():
    print(i)
print(person.items)









































