# _*_coding :utf-8 _*_
# @Time :2022/5/7 17:15
# @File : 016-python-type_conversion-bool()
# @Project : python-base

# 其他类型转为布尔类型

# 整型转换为布尔值。方法：bool().
"""
注意：在整数(包括正负）范围内，只有 0 转换为布尔值中的False
"""
a = 1
a = bool(a)
print(a)


# 浮点数转换为布尔值
"""
所有的浮点数都转换为True
"""
b = 2.22
b = bool(b)
# 第一次拼串成功，控制台输出True
print('b的类型为：' + str(b))


# 字符串转换为布尔值。
"""
注意：所有字符串都转换为True，包括空格字符串；
如果字符串内没有内容，将转换为False
"""
c = 'hello world！！'
c = bool(c)
print('c的类型为：' + str(c))


# list（列表）
"""
注意：只要列表里有数据就转换为True；
如果列表中什么数据都没有，就转换为False
"""
# 归国四子
d = ['吴亦凡', '黄子韬', '张艺兴', '鹿晗']
print('a的类型为：' + str(type(d)))
d = bool(d)
print('此时d的类型为：' + str(type(d)))

# tuple (元组）和列表一样
# dictionary (字典）也一样；


# 总结：
#    共有七种情况转换为布尔值False
#    1.bool(0)
#    2.bool(0.0)
#    3.bool('')
#    4.bool([])
#    5.bool(())
#    6.bool({})
#    7.bool("")














































